import logging

import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from .exceptions import PropertyNotFound
from .models import Property, PropertyViews
from .pagination import PropertyPagination
from .serializers import (
    PropertySerializers,
    PropertyViewSerializer,
    PropertyCreateSerializer,
)

logger = logging.getLogger(__name__)

"""
iexact :
    Case-insensitive exact match. If the value provided 
    for comparison is None, it will be interpreted as an SQL NULL
"""

"""
Filter allow for searching like that :
{{api url}}properties/all/?advert_type=For Rent
"""


class PropertyFilter(django_filters.FilterSet):
    advert_type = django_filters.CharFilter(
        field_name="advert_type", lookup_expr="iexact"
    )
    property_type = django_filters.CharFilter(
        field_name="property_type", lookup_expr="iexact"
    )

    """using in url : ?price__lt=4000 """
    price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name="price", lookup_expr="gt")
    price__lt = django_filters.NumberFilter(field_name="price", lookup_expr="lt")

    class Meta:
        model = Property
        fields = ["advert_type", "property_type", "price"]


class ListAllPropertiesAPIView(generics.ListAPIView):
    serializer_class = PropertySerializers
    queryset = Property.objects.all().order_by("-created_at")
    pagination_class = PropertyPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_class = PropertyFilter
    search_fields = ["country", "city"]
    ordering_fields = ["created_at"]


class ListAgentsPropertyAPIView(generics.ListAPIView):
    serializer_class = PropertySerializers
    pagination_class = PropertyPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = PropertyFilter
    search_fields = ["country", "city"]

    def get_queryset(self):
        user = self.request.user
        queryset = Property.objects.filter(user=user).order_by("-created_at")


class PropertyViewsAPIView(generics.ListAPIView):
    serializer_class = PropertyViewSerializer
    queryset = PropertyViews.objects.all()


class PropertyDetailView(APIView):
    """checking ip address and if not in db save it and increment views"""

    def get(self, request, slug):
        property = Property.objects.get(slug=slug)

        """ remote = machine address"""

        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")

        if not PropertyViews.objects.filter(property=property, ip=ip).exists():
            PropertyViews.objects.create(property=property, ip=ip)

            property.views += 1
            property.save()

        serializer = PropertySerializers(property, context={"request": request})

        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["PUT"])
@permission_classes([permissions.IsAuthenticated])
def update_property_api_view(request, slug):
    try:
        property = Property.objects.get(slug=slug)
    except Property.DoesNotExist:
        raise PropertyNotFound

    user = request.user
    if property.user != user:
        return Response(
            {"error": "You cant update or edit a property that doesn't belong to you"},
            status=status.HTTP_403_FORBIDDEN,
        )

    if request.method == "PUT":
        data = request.data
        serializer = PropertySerializers(property, data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def create_property_api_view(request):
    user = request.user
    data = request.data
    data["user"] = request.user.pkid
    serializer = PropertyCreateSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        logger.info(
            f'property {serializer.data.get("title")} created by {user.username}'
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([permissions.IsAuthenticated])
def delete_property_api_view(request, slug):
    try:
        property = Property.objects.get(slug=slug)
    except Property.DoesNotExist:
        raise PropertyNotFound

    user = request.user
    if property.user != user:
        return Response(
            {"error": "You cant delete a property that doesn't belong to you"},
            status=status.HTTP_403_FORBIDDEN,
        )

    if request.method == "DELETE":
        delete_operation = property.delete()
        data = {}
        if delete_operation:
            data["success"] = "Deletion was succesful"
        else:
            data["failure"] = "Delete failed"
        return Response(data=data)


@api_view(["POST"])
def uploadPropertyImage(request):
    data = request.data

    property_id = data["property_id"]
    property = Property.objects.get(id=property_id)
    property.cover_photo = request.FILE.get("cover_photo")
    property.photo1 = request.FILE.get("photo1")
    property.photo2 = request.FILE.get("photo2")
    property.photo3 = request.FILE.get("photo3")
    property.photo4 = request.FILE.get("photo4")
    property.save()
    return Response("Image(s) uploaded")


class PropertySearchAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PropertyCreateSerializer

    def post(self, request):
        queryset = Property.objects.filter(published_status=True)
        data = self.request.data

        advert_type = data["advert_type"]
        queryset = queryset.filter(advert_type__iexact=advert_type)

        property_type = data["property_type"]
        queryset = queryset.filter(property_type__iexact=property_type)

        price = data["price"]

        if price == "$0+":
            price = 0
        elif price == "$50,000+":
            price = 50000
        elif price == "$100,000+":
            price = 100000
        elif price == "$200,000+":
            price = 200000
        elif price == "$400,000+":
            price = 400000
        elif price == "$600,000+":
            price = 600000
        elif price == "Any":
            price = -1

        if price != -1:
            queryset = queryset.filter(price__gte=price)

        bedrooms = data["bedrooms"]
        if bedrooms == "0+":
            bedrooms = 0
        elif bedrooms == "1+":
            bedrooms = 1
        elif bedrooms == "2+":
            bedrooms = 2
        elif bedrooms == "3+":
            bedrooms = 3
        elif bedrooms == "4+":
            bedrooms = 4
        elif bedrooms == "5+":
            bedrooms = 5

        queryset = queryset.filter(bedrooms__gte=bedrooms)

        bathrooms = data["bathrooms"]
        if bathrooms == "0+":
            bathrooms = 0
        elif bathrooms == "1+":
            bathrooms = 1
        elif bathrooms == "2+":
            bathrooms = 2
        elif bathrooms == "3+":
            bathrooms = 3
        elif bathrooms == "4+":
            bathrooms = 4
        elif bathrooms == "5+":
            bathrooms = 5

        queryset = queryset.filter(bedrooms__gte=bathrooms)

        catch_phrase = data["catch_phrase"]
        queryset = queryset.filter(desciption__icontains=catch_phrase)

        serializer = PropertySerializers(queryset, many=True)

        return Response(serializer.data)

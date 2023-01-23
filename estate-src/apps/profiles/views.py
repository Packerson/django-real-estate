from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .exceptions import NotYourProfile, ProfileNotFound
from .models import Profile
from .renderers import ProfileJSONRenderer
from .serializers import ProfileSerializer, UpdatedProfileSerializer

"""
    Alternative version with method instead generics class views

    from rest_framework import api_view, permissions

    @api_view(["GET'])
    @permissions_classes((permissions.IsAuthenticated))
    def get_all_agent(request):
        agents = Profile.objects.filter(is_agent=True)
        serializer = ProfileSerializer.(agents, many = true)
        name_spaced_response = {"agents" : serializer.data}
        return Response(name_spaced_response, status=status.HTTP_200_OK)
"""


class AgentListApiView(generics.ListAPIView):

    """Generic list of Agents"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.filter(is_agent=True)
    serializer_class = ProfileSerializer


class TopAgentListApiView(generics.ListAPIView):

    """Generic list of top_agents"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.filter(top_agent=True)
    serializer_class = ProfileSerializer


class GetProfileApiView(APIView):

    """Generic profile View"""
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [ProfileJSONRenderer]

    def get(self, request):
        user = self.request.user
        user_profile = Profile.objects.get(user=user)
        serializer = ProfileSerializer(user_profile, context={"request": request})

        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateProfileApiView(APIView):

    """Generic update profile View with PATCH method"""
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [ProfileJSONRenderer]

    serializer_class = UpdatedProfileSerializer

    def patch(self, request, username):

        """PATCH: The PATCH method is used to apply partial modifications to a resource.

        Generally speaking, partial is used to check whether the fields in the model
        is needed to do field validation when client submitting data to the view."""

        try:
            Profile.objects.get(user__username=username)
        except Profile.DoesNotExist:
            raise ProfileNotFound

        user_name = request.user.username
        if user_name != username:
            raise NotYourProfile

        data = request.data
        serializer = UpdatedProfileSerializer(instance=request.user.profile, data=data,
                                              partial=True)

        serializer.is_valid()
        
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)





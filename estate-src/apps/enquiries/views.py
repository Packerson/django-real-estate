from django.core.mail import send_mail

from real_estate.settings.development import DEFAULT_FROM_EMAIL
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Enquiry


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def send_enquiry_email(request):
    data = request.data

    """Here is a problem:
        cannot send a email from email address that i dont have access. 
        as from_email write = info@sharpmind.club , and it's working """

    try:
        subject = data["subject"]
        name = data["name"]
        email = data["email"]
        message = data["message"]
        from_email = data["email"]
        # recipient_list = [DEFAULT_FROM_EMAIL]
        recipient_list = ["szachista49@gmail.com"]
        send_mail(subject, message, from_email, recipient_list, fail_silently=True)

        enquiry = Enquiry(name=name, email=email, subject=subject, message=message)
        enquiry.save()

        return Response({"success": "Your Enquiry was successfully submitted"})

    except:
        return Response({"fail": "Enquiry was not sent. Please try again."})

from django.core.mail import send_mail
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ContactSerializer


class ContactView(APIView):

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            email = validated_data.get('email')
            name = validated_data.get('name')
            send_mail(
                'Sent email from {}'.format(name),
                'Here is the message: {}'.format(serializer.validated_data.get('content')),
                email,
                ['to@example.com'],
                fail_silently=False,
            )
            return Response({"success": "Sent"})
        return Response({'success': "Failed"}, status=status.HTTP_400_BAD_REQUEST)

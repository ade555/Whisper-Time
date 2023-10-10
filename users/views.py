from rest_framework import generics, permissions
from dj_rest_auth.registration.views import RegisterView

from .models import User
from .serializers import UserSerializer

class UserRegistration(RegisterView):
    def get_response_data(self, user):
        return {
            'message': 'User successfully registered'
        }

    def register(self, request, *args, **kwargs):
        response = super().register(request, *args, **kwargs)
        if response.status_code == 201:
            response.data = self.get_response_data(self.user)
        return response


class UsersList(generics.ListAPIView):
    serializer_class = UserSerializer

    queryset = User.objects.all()

    permission_classes = (permissions.AllowAny,)

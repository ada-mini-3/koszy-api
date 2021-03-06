from rest_framework import viewsets, generics, \
                           authentication, permissions
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from userauth.serializers import RegisterSerializer, \
                                LoginSerializer, ProfileSerializer


class RegisterApiViewSet(viewsets.ViewSet):
    """ register api """
    serializer_class = RegisterSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        token, created = Token.objects.get_or_create(user=serializer.instance)

        return Response(
            {'token': token.key},
            status.HTTP_201_CREATED
        )


class LoginApiViewSet(ObtainAuthToken):
    """ login api """
    serializer_class = LoginSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ProfileApiViewSet(generics.RetrieveUpdateAPIView):
    """ get and update user profile """
    serializer_class = ProfileSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """ get the authenticated user data """
        return self.request.user

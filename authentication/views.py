from rest_framework.authtoken.views import ObtainAuthToken


class ObtainAuthTokenView(ObtainAuthToken):
    authentication_classes = ()

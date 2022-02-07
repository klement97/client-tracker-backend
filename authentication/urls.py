from django.urls import path

from authentication.views import ObtainAuthTokenView


urlpatterns = [
    path('token-login/', ObtainAuthTokenView.as_view())
]

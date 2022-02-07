from django.urls import include, path
from rest_framework.authtoken import views


urlpatterns = [
    path('', include('rest_framework.urls')),
    path('', include('clients.urls')),
    path('', include('authentication.urls')),
]

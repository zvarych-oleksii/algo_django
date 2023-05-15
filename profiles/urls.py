from django.urls import path, include


api_urlpatterns = [
    path('profiles/', include('rest_registration.api.urls')),
]

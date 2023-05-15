from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from profiles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/register', views.RegisterView.as_view(), name='register'),
    path('api/update/<int:user_id>', views.UpdateUserByIdView.as_view(), name='update_by_id'),
    path('api/get-user/<int:user_id>', views.UserProfileDetailViewById.as_view(), name='detail_user_by_id'),
    path('api/all-users/', views.UserProfileListView.as_view(), name='list_all_users')
]

from django.urls import path
from .views import (
    RegisterView,
    UpdateUserByIdView,
    UserProfileDetailViewById,
    UserProfileListView,
    DeleteUserView, UpdateSelfUserProfileView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('create/', RegisterView.as_view(), name='register'),
    path('update/<int:user_id>/', UpdateUserByIdView.as_view(), name='update_by_id'),
    path('<int:user_id>/', UserProfileDetailViewById.as_view(), name='detail_user_by_id'),
    path('list/', UserProfileListView.as_view(), name='list_all_users'),
    path('self/', UpdateSelfUserProfileView.as_view(), name='self_get_update'),
    path('delete/<int:user_id>', DeleteUserView.as_view(), name='delete-user'),
]

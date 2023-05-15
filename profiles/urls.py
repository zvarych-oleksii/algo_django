from django.urls import path
from .views import (
    RegisterView,
    UpdateUserByIdView,
    UpdateSelfUserView,
    UserProfileDetailViewById,
    SelfUserProfileView,
    UserProfileListView,

)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('update/<int:user_id>', UpdateUserByIdView.as_view(), name='update_by_id'),
    path('get/<int:user_id>', UserProfileDetailViewById.as_view(), name='detail_user_by_id'),
    path('all/', UserProfileListView.as_view(), name='list_all_users'),
    path('self/', SelfUserProfileView.as_view(), name='list_all_users'),
    path('self-update/', UpdateSelfUserView.as_view(), name='list_all_users')
]

from rest_framework.generics import (
    GenericAPIView,
    UpdateAPIView
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User

from .permission import IsStaffUser
from .serializers import (
    UserSerializer,
    RegisterUser,
    UpdateUserInformation
)


class RegisterView(GenericAPIView):
    serializer_class = RegisterUser

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,    context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })


class UpdateSelfUserView(UpdateAPIView):
    serializer_class = UpdateUserInformation
    permission_classes = [IsAuthenticated]
    def get_object(self):
        return self.request.user


class UpdateUserByIdView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserInformation
    permission_classes = [IsStaffUser]

    def get_object(self):
        user_id = self.kwargs['user_id']
        return User.objects.get(id=user_id)


class SelfUserProfileView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class UserProfileDetailViewById(GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        user_id = self.kwargs['user_id']
        return User.objects.get(id=user_id)

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class UserProfileListView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        instances = self.get_queryset()
        serializer = self.get_serializer(instances, many=True)
        return Response(serializer.data)

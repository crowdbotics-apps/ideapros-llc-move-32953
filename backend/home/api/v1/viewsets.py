from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from home.api.v1.serializers import (
    SignupSerializer,
    UserSerializer,
    UserProfileSerializer,
    UserProfileCreateSerializer,
)
from users.models import Profile


class UserProfileAPIView(APIView):
    def get(self, request):
        try:
            profile = Profile.objects.get(user=request.user)
            profile_serializer = UserProfileSerializer(profile)
            return Response(data=profile_serializer.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserProfileViewSet(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = Profile.objects.all()
    lookup_field = "user__id"
    filterset_fields = ("user__id",)

    def get_serializer_class(self):
        if self.request.method in ("POST"):
            return UserProfileCreateSerializer
        else:
            return UserProfileSerializer


class SignupViewSet(ModelViewSet):
    serializer_class = SignupSerializer
    http_method_names = ["post"]


class LoginViewSet(ViewSet):
    """Based on rest_framework.authtoken.views.ObtainAuthToken"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user)
        return Response({"token": token.key, "user": user_serializer.data})

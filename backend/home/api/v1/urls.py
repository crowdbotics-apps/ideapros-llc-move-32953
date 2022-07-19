from django.urls import path, include
from rest_framework.routers import DefaultRouter

from home.api.v1.viewsets import (
    UserProfileViewSet,
    UserProfileAPIView,
)

router = DefaultRouter()
router.register("profile", UserProfileViewSet, basename="profile")

urlpatterns = [
    path("", include(router.urls)),
    path("get-user-profile/", UserProfileAPIView.as_view()),
]

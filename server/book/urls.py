from django.urls import path, include

from rest_framework import routers

from .views import BookViewSet

router = routers.DefaultRouter()
router.register(r"", BookViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "book"

from django.urls import re_path, include
from rest_framework.routers import DefaultRouter
from CheckIn import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'CheckIn', views.CheckInViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls))
]
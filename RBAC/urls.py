from django.urls import re_path, include
from rest_framework.routers import DefaultRouter
from RBAC import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'User', views.UserViewSet)
router.register(r'Group', views.GroupViewSet)
router.register(r'Permission', views.PermissionViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls))
]
from django.urls import re_path, include
from rest_framework.routers import DefaultRouter
from Credit import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'Credit', views.CreditViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls))
]
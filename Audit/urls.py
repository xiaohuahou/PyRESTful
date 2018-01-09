from django.urls import re_path, include
from rest_framework.routers import DefaultRouter
from Audit import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'Book', views.BookViewSet)
router.register(r'Auditing', views.AuditingViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls))
]
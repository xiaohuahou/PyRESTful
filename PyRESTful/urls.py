"""PyRESTful URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='PyRESTful API')

urlpatterns = [
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^v1/RBAC/', include(('RBAC.urls','RBAC'), namespace='rbac_v1')),
    re_path(r'^v1/Audit/', include(('Audit.urls','Audit'), namespace='audit_v1')),
    re_path(r'^$', schema_view),
    path('admin/', admin.site.urls),
]

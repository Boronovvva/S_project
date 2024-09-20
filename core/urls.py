"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.users.views import logout_user


from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Clock",
      default_version='v1',
      description="Detailed descriptions of MyAPI.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="saraboronova003@gmail.com"),
      license=openapi.License(name="BSD License"),
      image=""  
   ),
   public=True,  
   permission_classes=(permissions.AllowAny,), 
)
api_urlpatterns = [
    path('', include('apps.clock.urls')),
    # path('users', include('apps.users.urls')),
    path('users/logout/', logout_user, name='logout_user'),
    # docs 
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name="api_swagger"),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name="api_redo")
]

urlpatterns = [
    path('admin/',admin.site.urls),
    path('api/', include(api_urlpatterns)),
    path('login/', TokenObtainPairView.as_view(), name='api_login'),
    path('refresh/', TokenRefreshView.as_view(), name='api_refresh'),
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

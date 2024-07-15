from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter
urlpatterns = [
    path('api/', include('amenities.urls')),
    path('api/', include('members.urls')),
    path('api/', include('staff.urls')),
    path('api/', include('settings.urls')),
    path('api/', include('contractors.urls')),
]

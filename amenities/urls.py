from django.urls import path
from .views import *

urlpatterns = [
    path('amenities/', AmenityView.as_view()),
    path('update-amenity/<int:pk>/', AmenityView.as_view()),
    path('amenity-reservations/', ReservationView.as_view()),
    path('update-amenity-reservation/<int:pk>/', ReservationView.as_view()),
    path('amenity-maintenance/', MaintenanceView.as_view()),
    path('amenity-maintenance/<int:pk>/', MaintenanceView.as_view()),
]
from django.urls import path
from .views import *

urlpatterns = [
#Amenity
    path('amenities/', AmenityView.as_view()),
    path('update-amenity/<int:pk>/', AmenityView.as_view()),
#Reservations
    path('amenity-reservations/', ReservationView.as_view()),
    path('update-amenity-reservation/<int:pk>/', ReservationView.as_view()),
#Maintenance
    path('amenity-maintenance/', MaintenanceView.as_view()),
    path('update-amenity-maintenance/<int:pk>/', MaintenanceView.as_view()),
]
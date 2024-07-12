from django.urls import path
from .views import * 

urlpatterns = [
    path('members/', MemberRegistrationView.as_view(), name='branch_stocks_detail'),
    path('add-new-member/', MemberRegistrationView.as_view(), name='add-new-member'),
]
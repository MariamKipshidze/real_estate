from django.urls import path

from application.views import property_list, property_detail

urlpatterns = [
    path('', property_list, name="property_list"),
    path('<int:pk>/', property_detail, name="property_detail"),
]

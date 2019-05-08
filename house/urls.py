from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="house-index"),
    path('<int:id>', views.get_house_by_id, name="house-details"),
    path('create_prop/', views.create_prop, name="house-create-prop")
]

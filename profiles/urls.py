from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="profile-index"),
    path('sell_property/', views.sell_property, name="profile-sell-property"),
    path('wishList/', views.wishList, name="profile-wishList"),
    path('history/', views.history, name="profile-history"),
    path('offers/', views.offers, name="profile-offers"),
    path('offers/<int:id>/', views.get_offer_by_id, name="offer-by-id"),
    path('myProps/', views.myProps, name="profile-myProps"),
    path('reviewPropertiesSubmissions/', views.reviewPropsSubs, name="profile-review-properties-submissions"),
    path('delUser/', views.delUser, name="profile-delete-user"),
    path('addAdmin/', views.addAdmin, name="profile-add-admin"),
    path('removeAdmin/', views.removeAdmin, name="profile-remove-admin"),
    path('editProperties/', views.editProps, name="profile-edit-properties"),
    path('deleteProperty/<int:id>/', views.delProperty, name="profile-delete-property")
]

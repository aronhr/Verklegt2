from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="profile-index"),
    path('sell_property/', views.sell_property, name="profile-sell-property"),
    path('wishList/', views.wish_list, name="profile-wishList"),
    path('history/', views.history, name="profile-history"),
    path('offers/', views.offers, name="profile-offers"),
    path('offers/<int:id>/', views.get_offer_by_id, name="offer-by-id"),
    path('myProps/', views.my_props, name="profile-myProps"),
    path('reviewPropertiesSubmissions/', views.review_props_subs, name="profile-review-properties-submissions"),
    path('delUser/', views.remove_user, name="profile-delete-user"),
    path('addAdmin/', views.add_admin, name="profile-add-admin"),
    path('removeAdmin/', views.remove_admin, name="profile-remove-admin"),
    path('editProperties/', views.edit_props, name="profile-edit-properties"),
    path('deleteProperty/<int:id>/', views.del_property, name="profile-delete-property"),
    path('deletewish/<int:id>/', views.remove_wish, name="profile-delete-wish")
]

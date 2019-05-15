from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="profile-index"),
    path('sell_property/', views.sell_property, name="profile-sell-property"),
    path('wishList/', views.wish_list, name="profile-wishList"),
    path('history/', views.history, name="profile-history"),
    path('offers/', views.offers, name="profile-offers"),
    path('approveoffer/<int:id>/', views.approve_offer, name="profile-approve-offer"),
    path('declineoffer/<int:id>/', views.decline_offer, name="profile-decline-offer"),
    path('myProps/', views.my_props, name="profile-myProps"),
    path('reviewPropertiesSubmissions/', views.review_props_subs, name="profile-review-properties-submissions"),
    path('delUser/', views.remove_user, name="profile-delete-user"),
    path('addAdmin/', views.add_admin, name="profile-add-admin"),
    path('removeAdmin/', views.remove_admin, name="profile-remove-admin"),
    path('editProperties/', views.edit_props, name="profile-edit-properties"),
    path('deleteProperty/<int:id>/', views.del_property, name="profile-delete-property"),
    path('deletewish/<int:id>/', views.remove_wish, name="profile-delete-wish"),
    path('approvesubmission/<int:id>/', views.approve_submission, name="profile-approve-submission"),
    path('declinesubmission/<int:id>/', views.decline_submission, name="profile-decline-submission"),
    path('buy_property/<int:id>', views.buy_property, name="profile-buy-property"),
    path('delUser/<int:id>/', views.remove_user_id, name="profile-remove-user-id"),
    path('removeAdmin/<int:id>/', views.remove_admin_id, name="profile-remove-admin-id"),
    path('addAdmin/<int:id>/', views.add_admin_id, name="profile-add-admin-id"),
    path('addHouseToWishList/<int:id>/', views.add_to_wish_list, name="profile-add-to-wish-list")
]

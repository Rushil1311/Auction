from django.urls import path

from . import views
from auctions.views import add_category, aview_profile, delete_category, edit_category, feedback_delete, feedback_page, initiate_payment, manage_category, payment_list, payment_success,submit_feedback, view_feedback, view_profile

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("category/", views.categories, name="categories"),
    path("category/<str:category>/", views.category, name="category"),
    path("create_listing/", views.create_listing, name="create_listing"),
    path("your_listings/", views.your_listings, name="your_listings"),
    path("won_listings/", views.won_listings, name="won_listings"),
    path("watch_list/", views.watch_list, name="watch_list"),
    path("listing/<int:listing_id>/", views.view_listing, name="listing"),
    path("listing/<int:listing_id>/watch/", views.watch, name="watch"),
    path("listing/<int:listing_id>/close/", views.close_auction, name="close_auction"),
    path("listing/<int:listing_id>/bid/", views.bid, name="bid"),
    path("listing/<int:listing_id>/comment/", views.comment, name="comment"),
    path('otp-verification/', views.otp_verification, name='otp_verification'),
    path('otp-success/', views.otp_success, name='otp_success'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('forgot-password-otp/', views.password_otp, name='password_otp'),
    path('reset-password/', views.password_reset_success, name='password_reset_success'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/edit/password/', views.edit_password, name='edit_password'),
    path('admin-dashboard/', views.admin_view, name='admin_view'),
    path("admin-dashboard/manage-users", views.manage_users, name="manage_users"),
    path("admin-dashboard/manage-lisitngs", views.manage_listings, name="manage_listings"),
    path('deactivate_listing/<int:listing_id>/', views.deactivate_listing, name='deactivate_listing'),
    path('delete_listing/<int:listing_id>/', views.delete_listing, name='delete_listing'),
    path("admin-dashboard/reports", views.reports, name="reports"),
    path('forbidden/', views.forbidden_view, name='forbidden'),
    path('feedback/', feedback_page, name='feedback'),
    path('submit-feedback/', submit_feedback, name='submit_feedback'),
    path('view_feedback/', view_feedback, name='view_feedback'),
    path('feedback_delete/<int:id>/', feedback_delete, name='feedback_delete'),
    path('aview_profile/', aview_profile, name='aview_profile'),
    path('manage_category/', manage_category, name='manage_category'),

    path("manage-category/", manage_category, name="manage_category"),
    path("add_category/", add_category, name="add_category"),
    path("edit_category/<int:category_id>/", edit_category, name="edit_category"),
    path("delete_category/<int:category_id>/", delete_category, name="delete_category"),


     path("initiate-payment/<int:listing_id>/", initiate_payment, name="initiate_payment"),
     path("payment-success/", payment_success, name="payment_success"),
     path("payments/", payment_list, name="payment_list"),


]

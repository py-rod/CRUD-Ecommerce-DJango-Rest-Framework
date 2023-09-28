from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView


urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("signin/", views.Signin.as_view(), name="signin"),
    path("logout/", views.logout_view, name="logout"),
    path("resfresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("profile/", views.get_user_profile, name="get_user_profile"),
    path("profile/update/", views.update_user_profile, name="update_user_profile"),
    # GET ALL USER ADMIN
    path("allusers/", views.get_all_users, name="get_all_users"),
    # GET USER BY ID ADMIN
    path("profile/user/<pk>/", views.get_user_by_id_admin,
         name="get_user_by_id_admin"),
    # DELETE USER, ADMIN
    path("profile/delete/<pk>/", views.delete_user, name="delete_user")
]

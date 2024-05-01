from django.urls import path

from .views import UserListView

urlpatterns = [
    path("v1/auth/users/", UserListView.as_view(), name="user-list"),
    path("v1/auth/users/<str:username>/", UserListView.as_view(), name="user-list"),
]

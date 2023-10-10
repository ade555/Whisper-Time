from django.urls import path

from .views import UsersList

urlpatterns = [
    path('', UsersList.as_view(), name="all-users")
]
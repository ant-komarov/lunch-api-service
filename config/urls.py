from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/user/", include("user.urls", namespace="user")),
    path("api/v1/", include("restaurant.urls", namespace="restaurant")),
    path("api/v1/", include("vote.urls", namespace="vote")),
]

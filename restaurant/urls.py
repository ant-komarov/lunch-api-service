from django.urls import path, include
from rest_framework import routers

from restaurant.views import RestaurantViewSet, DishViewSet, MenuViewSet

router = routers.DefaultRouter()
router.register("restaurants", RestaurantViewSet)
router.register("dishes", DishViewSet)
router.register("menus", MenuViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "restaurant"

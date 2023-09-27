import datetime

from rest_framework import mixins
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import GenericViewSet

from restaurant.models import Restaurant, Dish, Menu
from restaurant.permissions import IsAdminOrIfAuthenticatedReadOnly
from restaurant.serializers import RestaurantSerializer, DishSerializer, MenuSerializer, MenuDetailSerializer


class RestaurantViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (IsAdminUser,)


class DishViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = (IsAdminUser,)


class MenuViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

    def get_queryset(self):
        queryset = self.queryset
        if not self.request.user.is_staff:
            queryset = queryset.filter(date=datetime.date.today())
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return MenuDetailSerializer
        return self.serializer_class

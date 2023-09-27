from rest_framework import serializers

from restaurant.models import Restaurant, Dish, Menu


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ("name",)


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ("name", "weight", "price")


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ("id", "date", "restaurant", "dishes")


class MenuDetailSerializer(MenuSerializer):
    restaurant = RestaurantSerializer(read_only=True)
    dishes = DishSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = ("id", "date", "restaurant", "dishes")

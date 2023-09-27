from rest_framework import serializers

from restaurant.serializers import MenuDetailSerializer
from user.serializers import UserInfoSerializer
from vote.models import Vote


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ("id", "menu", "user")


class VoteDetailSerializer(VoteSerializer):
    menu = MenuDetailSerializer(read_only=True)
    user = UserInfoSerializer(read_only=True)

    class Meta:
        model = Vote
        fields = ("id", "menu", "user")

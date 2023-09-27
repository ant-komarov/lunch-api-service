from django.db.models import Count
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from restaurant.models import Menu
from restaurant.serializers import MenuDetailSerializer
from vote.models import Vote
from vote.serializers import VoteSerializer, VoteDetailSerializer


class VoteView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        today = timezone.now().date()
        user = request.user
        try:
            vote = Vote.objects.get(user=user, date=today)
        except Vote.DoesNotExist:
            return Response({"message": "You haven't voted yet"})
        serializer = VoteDetailSerializer(vote)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        today = timezone.now().date()
        data = request.data
        user = request.user
        data["user"] = user.id
        try:
            vote = Vote.objects.get(user=user, date=today)
        except Vote.DoesNotExist:
            serializer = VoteSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if vote:
            return Response({"message": "You've already voted today"})


class ResultView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        today = timezone.now().date()
        queryset = Menu.objects.filter(date=today)
        menu_id_with_max_votes = (
            Vote.objects.filter(date=today)
            .values('menu_id')
            .annotate(vote_count=Count('menu_id'))
            .order_by('-vote_count')
        ).first()
        if menu_id_with_max_votes:
            queryset = queryset.get(id=menu_id_with_max_votes['menu_id'])

        serializer = MenuDetailSerializer(queryset)

        return Response(serializer.data, status=status.HTTP_200_OK)

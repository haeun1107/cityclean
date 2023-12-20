from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TrashCans
from .serializers import TrashCanSerializer, TrashCanListSerializer, TrashCansListSerializer

class TrashCanCreateView(APIView):

    def post(self, request):
        data = request.data
        serializer = TrashCanSerializer(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class TrashCanListView(APIView):
    def get(self, request):
        # 유저 1이 작성한 쓰레기통만 필터링
        trash_cans_queryset = TrashCans.objects.filter(user=1) ###
        serializer = TrashCanListSerializer(trash_cans_queryset, many=True)
        return Response(serializer.data)

class TrashCansView(APIView):
    def get(self, request):
        trash_cans_queryset = TrashCans.objects.all()
        serializer = TrashCansListSerializer(trash_cans_queryset, many=True)
        return Response(serializer.data)
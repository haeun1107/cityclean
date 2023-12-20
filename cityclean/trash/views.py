from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Trash
from .serializers import TrashListSerializer, TrashSerializer,TrashListsSerializer

class TrashCreateView(APIView):

    def post(self, request):
        data = request.data
        serializer = TrashSerializer(data=data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class TrashsView(APIView):
    def get(self, request):
        trash_queryset = Trash.objects.all()
        serializer = TrashListSerializer(trash_queryset, many=True)
        return Response(serializer.data)

class TrashListView(APIView):
    def get(self, request):
        trash_queryset = Trash.objects.all()
        serializer = TrashListsSerializer(trash_queryset, many=True)
        return Response(serializer.data)

class DeletetrashView(APIView):
    def get_object(self, pk):
        try:
            return Trash.objects.get(pk=pk)
        except Trash.DoesNotExist:
            return None

    def delete(self, request, pk):
        trash = self.get_object(pk)
        if trash:
            trash.delete()
            return Response({'message': 'Trash deleted'})
        return Response({'message': 'Trash not found'}, status=404)
import json

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Declaration
from .serializers import DeclarationSerializer
from user.models import User
from trashcan.models import TrashCans

class DeclarationView(APIView):
    def post(self, request):
        # Get Data From Request By Body(JSON)
        data = json.loads(request.body.decode('utf-8'))
        
        # Read And Validate User, TrashCan
        user = User.objects.get(id=1) ###
        trashCans = TrashCans.objects.get(id=data['trashCanId'])
        declarations = Declaration.objects.filter(user=user, trashCans=trashCans)
        
        if declarations.exists():
            return Response({'error': 'You have already declared this trash can'}, status=400)
        
        # Create Declaration With Dict Data
        serializer = DeclarationSerializer(
            data=data,
            context={
                'user': user,
                'trashCans': trashCans})
        
        ## Validate Declaration
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        
        # Save Declaration
        serializer.save()
        
        # Find DeClartion By TrashCan
        declarations = Declaration.objects.filter(trashCans=trashCans)
        
        # If Declaration Count Is 2, Delete TrashCan
        if declarations.count() >= 2:
            trashCans.delete()
            
        return Response(serializer.data, status=201)
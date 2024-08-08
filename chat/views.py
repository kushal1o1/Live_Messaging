from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .models import Message
from .serializers import UserSerializer, MessageSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MessageViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Message.objects.all()
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @action(detail=False, methods=['get'])
    def between_users(self, request):
        sender_id = request.query_params.get('sender')
        receiver_id = request.query_params.get('receiver')
        queryset = Message.objects.filter(sender_id=sender_id, receiver_id=receiver_id)
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)

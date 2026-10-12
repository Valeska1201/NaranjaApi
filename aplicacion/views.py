from django.shortcuts import render
from .serializers import PostreSerializer
from .models import Postre
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def postre_list(request):
    if request.method == 'GET':
        postres =Postre.objects.all()
        serializer = PostreSerializer(postres, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = PostreSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def postre_detail(request, pk):
    try:
        postre = Postre.objects.get(pk=pk)
    except Postre.DoesNotExist:
        return Response({"error": "Postre no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostreSerializer(postre)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = PostreSerializer(postre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        postre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        
from django.shortcuts import render

# Create your views here.
from .models import Bugs
from .serializer import BugSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def hello(request):
  if request.method == 'GET':
    bugs = Bugs.objects.all()
    serializer = BugSerializer(bugs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  else:
    serializer = BugSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
  
@api_view(['GET', 'PUT', 'DELETE'])  
def get_by_id(request, id):
  try:
    data = Bugs.objects.get(pk=id)
  except Bugs.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    data_serial = BugSerializer(data)
    return Response(data_serial.data, status=status.HTTP_200_OK)
  elif request.method == 'PUT':
    data_serial = BugSerializer(data, request.data)
    if data_serial.is_valid():
      data_serial.save()
      return Response(data_serial.data, status=status.HTTP_200_OK)
    return Response(data_serial.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
    data.delete()
    return Response(status=status.HTTP_200_OK)
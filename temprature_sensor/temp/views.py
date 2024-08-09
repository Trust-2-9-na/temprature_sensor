from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import SensorData
from .serializers import SensorDataSerializer
from rest_framework import status

def index(request):
    sensor_data = SensorData.objects.all()
    serializer = SensorDataSerializer(sensor_data, many=True)
    context = {
        'sensor_data': serializer.data
    }
    return render(request, 'temp/index.html', context)

class SensorDataList(APIView):
    def get(self, request, *args, **kwargs):
        sensor_data = SensorData.objects.all()
        serializer = SensorDataSerializer(sensor_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = SensorDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
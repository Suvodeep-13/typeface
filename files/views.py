from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from django.http import FileResponse
from .models import File
from .serializers import FileSerializer, FileUploadSerializer
import os


class FileUploadView(APIView):
    def post(self, request):
        serializer = FileUploadSerializer(data=request.data)

        # validate the input data
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        file = serializer.validated_data['file']
        name = serializer.validated_data['name']
        size = file.size
        file_type = os.path.splitext(file.name)[1][1:]  # Get file extension
        
        file_obj = File.objects.create(
            file=file,
            name=name,
            size=size,
            file_type=file_type
        )
        return Response(FileSerializer(file_obj).data, status=status.HTTP_201_CREATED)
    

class FileDetailView(APIView):

    def get_object(self, file_id):
        try:
            return File.objects.get(id=file_id)
        except File.DoesNotExist:
            return None

    def get(self, request, file_id):
        file_obj = self.get_object(file_id)
        if file_obj is None:
            return JsonResponse({'message':'File not found.'},status=status.HTTP_404_NOT_FOUND)
        
        file_path = file_obj.file.path
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=file_obj.name)

    def put(self, request, file_id):
        file_obj = self.get_object(file_id)
        if file_obj is None:
            return Response({'message':'File not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = FileUploadSerializer(file_obj, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        if 'file' in serializer.validated_data:
            file = serializer.validated_data['file']
            file_obj.size = file.size
            file_obj.file_type = os.path.splitext(file.name)[1][1:]
        serializer.save()
        return Response(FileSerializer(file_obj).data)

    def delete(self, request, file_id):
        file_obj = self.get_object(file_id)
        if file_obj is None:
            return Response({'message':'File not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        file_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FileListView(APIView):
    def get(self, request):
        files = File.objects.all()  
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data)
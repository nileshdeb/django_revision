from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

class StudentAPI(APIView):
    def get(self, request,pk=None):
       if pk:
        try:
            student=Student.objects.get(id=pk) 
            serializer=StudentSerializer(student)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({'message':'Student not found'},status=status.HTTP_404_NOT_FOUND)
       else:
        students=Student.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

#Create data (post)
    def post(self, request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#Update data (put)
    def put(self, request,pk=None):
        try:
            student=Student.objects.get(id=pk) 
            serializer=StudentSerializer(student,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Student.DoesNotExist:
            return Response({'message':'Student not found'},status=status.HTTP_404_NOT_FOUND)

#Delete data (delete)
    def delete(self, request,pk=None):
        try:
            student=Student.objects.get(id=pk) 
            student.delete()
            return Response({'message':'Student deleted'},status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({'message':'Student not found'},status=status.HTTP_404_NOT_FOUND)

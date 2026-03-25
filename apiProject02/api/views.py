from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer

@api_view(['GET'])
def get_students(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)    

@api_view(['POST'])
def add_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT','PATCH'])
def update_student(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return Response(status=404)
    # partial update
    if request.method == 'PATCH':
        serializer = StudentSerializer(student, data=request.data, partial=True)
    else:    
        serializer = StudentSerializer(student, data=request.data)


    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_student(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return Response(status=404)
    student.delete()
    return Response(status=204)  
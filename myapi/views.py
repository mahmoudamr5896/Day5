from http.client import NOT_FOUND
from telnetlib import STATUS
from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

# Create your views here.
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from company.models import Epmloyee ,TeamLeader
from .serilaizares import EmployeeSerializer, EmployeeSerilazer

@api_view(['GET', 'POST'])
def MyAPIView(request):
        # data=Epmloyee.objects.all()
        # seralizer=EmployeeSerilazer(data,many=True)
        # return Response(seralizer.data)
        if request.method == 'GET':
              emps =Epmloyee.objects.all()
              seralizer=EmployeeSerilazer(emps,many=True)
              return Response(seralizer.data)
       
        if request.method == 'POST':
            data=request.data
            seralizer=EmployeeSerilazer(data=data)
            if seralizer.is_valid():
                seralizer.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
# calsses base view 
# @api_view(["GET", "POST"])
            

class MyAPIView2(APIView):
    def get(self,request):
        Epmloyees=Epmloyee.objects.all()
        seralizer=EmployeeSerilazer(Epmloyees,many=True)
        return Response(seralizer.data)
    
    def post(self,request):
        data=request.data
        seralizer=EmployeeSerilazer(data=data)
        if seralizer.is_valid():
            seralizer.save()
            Epmloyees=Epmloyee.objects.all()
            all_data=EmployeeSerilazer(seralizer.data)
            return Response({"emplyees":all_data.data},status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        employee_id = request.data.get('id')
        try:
            employee = Epmloyee.objects.get(pk=employee_id)
        except Epmloyee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        employee_id = request.data.get('id')
        try:
            employee = Epmloyee.objects.get(pk=employee_id)
        except Epmloyee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   
    
    def get(self, request, pk):
        try:
            employee = Epmloyee.objects.get(pk=pk)
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data)
        except Epmloyee.DoesNotExist:
            raise NOT_FOUND(detail="Employee not found", code=status.HTTP_404_NOT_FOUND)


#   view set       
class MyAPIView3(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = EmployeeSerilazer
    queryset = Epmloyee.objects.all()
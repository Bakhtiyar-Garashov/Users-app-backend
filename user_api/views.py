from django.shortcuts import render
from rest_framework.views import APIView
import json
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
# Create your views here.

class Users(APIView):  
    def get(self,request):
        """GET all user objects"""
        try:
            json_file=open('users.json')
            data = json.load(json_file)
            json_file.close()
            return Response(data,status=status.HTTP_200_OK)
        except:
            return Response({"failed":"error occured while fetching data"},status=status.HTTP_400_BAD_REQUEST)
       

    def post(self,request):
        """POST a new user object"""
        try:
            file_handler=open('users.json')
            data = json.load(file_handler)
            file_handler.close()
            json_file=open('users.json','w+')
            new_obj=request.data
            data['users'].append(new_obj)
            json.dump(data,json_file)
            return Response({"success":"new object created successfully"},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"failed":str(e)},status=status.HTTP_400_BAD_REQUEST)


   

class UsersDetail(APIView):
    
    def get(self,request,id):
        """GET an user object"""
        try:
            file_handler=open('users.json')
            data = json.load(file_handler)
            file_handler.close()

            for each_entry in data['users']:
                if each_entry["id"]==id:
                    return Response(each_entry)
            return Response({"failed":"object doesn't exist"},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"failed":str(e)},status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request,id):
        """PUT an user object"""
        try:
            file_handler=open('users.json')
            data = json.load(file_handler)
            file_handler.close()
            for each_entry in data['users']:
                if each_entry["id"]==id:
                    data['users'].remove(each_entry)
                    data['users'].append(request.data)
                    json_file=open('users.json','w+')
                    json.dump(data,json_file)
                    json_file.close()
                    return Response({"success":"updated successfully"},status=status.HTTP_200_OK)
            return Response({"failed":"failed to update"})
        except Exception as e:
            return Response({"failed":str(e)},status=status.HTTP_400_BAD_REQUEST)



    def delete(self,request,id):
        """DELETE an user object"""
        try:
            file_handler=open('users.json')
            data = json.load(file_handler)
            file_handler.close()
            for each_entry in data['users']:
                if each_entry['id']==id:
                    data['users'].remove(each_entry)
                    json_file=open('users.json','w+')
                    json.dump(data,json_file)
                    json_file.close()
                    return Response({"success":"deleted successfully"},status=status.HTTP_200_OK)
            return Response({"failed":"failed to update"})
        except Exception as e:
             return Response({"failed":str(e)},status=status.HTTP_400_BAD_REQUEST)





        
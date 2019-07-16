from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .serializers import CreateUserSerializer,all_username
from rest_framework import status
from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny,IsAuthenticated
import requests

CLIENT_ID = 'NAqmM6DgztIkVi898JqJDSBbw0f8HrHVBbP1o5Wf'
CLIENT_SECRET = 'Y1KIhtHtQGGza7ACfNyMTltFmVgk9NPetizNDPNjTiEDpkHZJ9SeY9eb3AYS8OFAO7KKABrFcLNfZgSXXuWKs7io3hk3CYIM4uw5kDVs0QPwlh7gjiHzL374hpEl1ibl'
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
        '''
        Registers user to the server. Input should be in the format:
        {"username": "username", "password": "1234abcd","first_name":"first","last_name":"last"}
        '''
        # Put the data from the request into the serializer 
        serializer = CreateUserSerializer(data=request.data) 
        # Validate the data
        if serializer.is_valid():
                # If it is valid, save the data (creates a user).
                serializer.save() 
                # Then we get a token for the created user.
                # This could be done differentley 
                d = request.data
                
                r = requests.post('http://127.0.0.1:8000/o/token/', 
                        data={
                                'username':request.data['username'],
                                'password':request.data['password'],
                                'first_name':request.data['first_name'],
                                'last_name':request.data['last_name'],
                                'email':request.data['email'],
                                'client_id':CLIENT_ID,
                                'client_secret' : CLIENT_SECRET,
                                'grant_type' : 'password'

                        }
                )
                return Response(r.json())
        return Response(serializer.errors)



@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    
        d = request.data

        
        r = requests.post('http://127.0.0.1:8000/o/token/', 
                data={
                                'client_id' : CLIENT_ID,
                                'client_secret' : CLIENT_SECRET,
                                'grant_type' : 'password',
                                'username':request.data['username'],
                                'password':request.data['password']
                }       
        )
        return Response(r.json())



@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    '''
    Registers user to the server. Input should be in the format:
    {"refresh_token": "<token>"}
    '''
    r = requests.post(
    'http://127.0.0.1:8000/o/token/', 
        data={
            'grant_type': 'refresh_token',
            'refresh_token': request.data['refresh_token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(r.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def revoke_token(request):
    '''
    Method to revoke tokens.
    {"token": "<token>"}
    '''
    r = requests.post(
        'http://127.0.0.1:8000/o/revoke_token/', 
        data={
            'token': request.data['token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    # If it goes well return sucess message (would be empty otherwise) 
    if r.status_code == requests.codes.ok:
        return Response({'message': 'token revoked'}, r.status_code)
    # Return the error if it goes badly
    return Response(r.json(), r.status_code)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_username(request):
        if request.method == 'GET':
                user = request.user
                return Response({"id":user.id})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_username(request):
        u = User.objects.filter()
        
        serializer = all_username(u,many = True)
        for i in serializer.data:
                i['label'] = i['username']
                i['value'] = i['id']
        return Response(serializer.data)



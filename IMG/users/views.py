from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .serializers import CreateUserSerializer
from rest_framework import status
from django.utils import timezone
from rest_framework.permissions import AllowAny
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
                d['client_id'] = CLIENT_ID
                d['client_secret'] = CLIENT_SECRET
                d['grant_type'] = 'password'
                r = requests.post('http://127.0.0.1:8000/o/token/', 
                        data=d
                )
                return Response(r.json())
        return Response(serializer.errors)



@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    
        d = request.data
        d['client_id'] = CLIENT_ID
        d['client_secret'] = CLIENT_SECRET
        d['grant_type'] = 'password'
        
        r = requests.post('http://127.0.0.1:8000/o/token/', 
                data=d,
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
        'http://127.0.0.:8000/o/revoke_token/', 
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

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.contrib.auth import authenticate, login


@api_view(['POST'])
def registration_api_view(request):
    if request.method == 'POST':
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if not (username and email and password):
            return Response({'error': 'Username, email, and password are required'},
                            status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'},
                            status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email address already registered'},
                            status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username,
                                        email=email,
                                        password=password,
                                        is_active=False)

        confirmation_code = get_random_string(length=6)
        user.confirmation_code = confirmation_code
        user.save()

        return Response({'success': 'User registered successfully. Confirmation code sent to your email.'},
                        status=status.HTTP_201_CREATED)


@api_view(['POST'])
def login_api_view(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response({'success': 'User logged in successfully.'},
                            status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid username or password'},
                            status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def confirmation_api_view(request):
    if request.method == 'POST':
        confirmation_code = request.data.get('confirmation_code')

        if not confirmation_code:
            return Response({'error': 'Confirmation code is required'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(confirmation_code=confirmation_code)
        except User.DoesNotExist:
            return Response({'error': 'Invalid confirmation code'},
                            status=status.HTTP_400_BAD_REQUEST)

        user.is_active = True
        user.save()

        return Response({'success': 'User confirmed successfully'},
                        status=status.HTTP_200_OK)

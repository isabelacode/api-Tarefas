from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import (
    UserRegistrationSerializer, 
    UserSerializer, 
    UserLoginSerializer,
    PasswordResetRequestSerializer,
    PasswordResetConfirmSerializer
)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    """
    Endpoint para criação de nova conta de usuário
    """
    serializer = UserRegistrationSerializer(data=request.data)
    
    if serializer.is_valid():
        user = serializer.save()
        user_serializer = UserSerializer(user)
        
        return Response({
            'message': 'Usuário criado com sucesso!',
            'user': user_serializer.data
        }, status=status.HTTP_201_CREATED)
    
    return Response({
        'message': 'Erro ao criar usuário',
        'errors': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    """
    Endpoint para login com JWT
    """
    serializer = UserLoginSerializer(data=request.data)
    
    if serializer.is_valid():
        user = serializer.validated_data['user']
        
        refresh = RefreshToken.for_user(user)
        access_token = refresh.access_token
        
        user_serializer = UserSerializer(user)
        
        return Response({
            'message': 'Login realizado com sucesso!',
            'user': user_serializer.data,
            'tokens': {
                'access': str(access_token),
                'refresh': str(refresh),
            }
        }, status=status.HTTP_200_OK)
    
    return Response({
        'message': 'Erro no login',
        'errors': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def password_reset_request(request):
    """
    Endpoint para solicitar redefinição de senha
    """
    serializer = PasswordResetRequestSerializer(data=request.data)
    
    if serializer.is_valid():
        result = serializer.save()
        return Response(result, status=status.HTTP_200_OK)
    
    return Response({
        'message': 'Erro ao solicitar redefinição de senha',
        'errors': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def password_reset_confirm(request, uidb64, token):
    """
    Endpoint para confirmar redefinição de senha
    """
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        return Response({
            'message': 'Link de redefinição inválido'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    if not default_token_generator.check_token(user, token):
        return Response({
            'message': 'Token de redefinição inválido ou expirado'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = PasswordResetConfirmSerializer(data=request.data)
    if serializer.is_valid():
        user.set_password(serializer.validated_data['new_password'])
        user.save()
        
        return Response({
            'message': 'Senha redefinida com sucesso!'
        }, status=status.HTTP_200_OK)
    
    return Response({
        'message': 'Erro ao redefinir senha',
        'errors': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_profile(request):
    """
    Endpoint para obter dados do usuário logado
    """
    if request.user.is_authenticated:
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
    return Response({
        'message': 'Usuário não autenticado'
    }, status=status.HTTP_401_UNAUTHORIZED)

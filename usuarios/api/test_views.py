from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def test_endpoint(request):
    return Response({
        'method': request.method,
        'message': 'Test endpoint funcionando',
        'data': request.data if request.method == 'POST' else None
    }, status=status.HTTP_200_OK)

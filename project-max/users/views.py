from rest_framework import status,permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import RegisterUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        reg_serializer = RegisterUserSerializer(data=request.data)
        if reg_serializer.is_valid():
            newuser = reg_serializer.save()
            if newuser:
                return Response(data="User Created",status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class BlacklistTokenView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(data="Logout Successful", status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class getUser(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def get(self, request):
        user = self.request.user
        if user:
            user_data = {
                'user_id': user.id,
                'email': user.email,
                'user_name':user.user_name,
                'first_name':user.first_name,
                'last_name':user.last_name, 
                'start_date':user.start_date, 
                'is_staff': user.is_staff, 
                'is_active': user.is_active
            }
            return Response(user_data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Usuario no autenticado'}, status=status.HTTP_401_UNAUTHORIZED)
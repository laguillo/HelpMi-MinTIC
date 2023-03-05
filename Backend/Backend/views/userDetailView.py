from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from Backend.models.user import User
from Backend.serializers.userSerializer import UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().get(request, *args, **kwargs)

#>>>Está dando error<<<
# from rest_framework import generics, status
# from rest_framework.response import Response
# #from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from serializers.userSerializer import UserSerializer
# from models.user import User

# class UsuarioListView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     #permission_classes = (IsAuthenticated,)

#     def list(self, request):
#         print("GET a todos los User")
#         queryset = self.get_queryset()
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)

# class UsuarioRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     lookup_field = "id"             # campo con el que se realiza la búsqueda de los objetos
#     lookup_url_kwarg = 'pk'         # nombre dado en la url al argumento
#     #permission_classes = (IsAuthenticated,)

#     def get(self, request, *args, **kwargs):
#         print("GET a User")
#         """ if valid_data['user_id'] != kwargs['pk']:
#             stringResponse = {'detail':'Unauthorized Request'}
#             return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
#         return super().get(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         print("PUT a User")
#         """ if valid_data['user_id'] != kwargs['pk']:
#             stringResponse = {'detail':'Unauthorized Request'}
#             return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
#         return super().put(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         print("DELETE a User")
#         """ if valid_data['user_id'] != kwargs['pk']:
#             stringResponse = {'detail':'Unauthorized Request'}
#             return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
#         return super().delete(request, *args, **kwargs)
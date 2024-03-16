from django.contrib.auth.models import User
from django.core.cache import cache
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CategorySerializer, ProductSerializer, UserLoginSerializer
from apps.models import Category, Product
from apps.serializers import RegisterSerializer
from apps.email_send_masage import send_verification_email
class RegisterCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def get_success_headers(self, data):
        import uuid
        _uuid = uuid.uuid4()
        send_verification_email(data['email'], _uuid.__str__())
        cache.set(_uuid, data['email'])
        print('sent email!')
        return super().get_success_headers(data)


class ConfirmEmailAPIView(APIView):
    def get(self, request, pk):
        email = cache.get(pk)
        User.objects.filter(email=email).update(is_active=True)
        return Response({'message': 'User confirmed email!'})





class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_fields = ('name',)

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class UserLoginAPIView(ObtainAuthToken):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer




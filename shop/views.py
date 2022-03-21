from rest_framework import status
from rest_framework.response import Response

from shop.serializers import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView


class ProductListApiView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductObjectApiView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]

        return Product.objects.filter(id=pk)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class CategoryListApiView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class ListProductCategory(ListCreateAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Product.objects.filter(category=pk)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


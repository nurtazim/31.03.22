from rest_framework import serializers
from shop.models import *


class CategorySerializers(serializers.ModelSerializer):
    title = serializers.CharField(required=True)

    class Meta:
        model = Category
        fields = ("id", "title", "children")


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product

        fields = ("id","image","price", "title", "content", "category", "slug","stock")

from rest_framework import serializers  

from .model import ItemImageModelSerializer, ItemModelSerializer
from ..models import ItemModel
from apps.categories.serializers import CategoryModelSerializer
from apps.storage.serializers import StorageResponseSerializer


class ItemResponseSerializer(serializers.ModelSerializer):
    category = CategoryModelSerializer()
    storage = StorageResponseSerializer()
    created_at = serializers.DateField(format='%d.%m.%Y')
    images = ItemImageModelSerializer(source="image_item_for_items", many=True)

    class Meta:
        model = ItemModel
        fields = [
            'id', 
            'name', 
            'description', 
            'created_at', 
            'category', 
            'storage',
            'images',
        ]
        
        
# class ItemResponseSerializer(serializers.Serializer):
#     item = ItemModelSerializer()
#     images = ItemImageModelSerializer(source="image_item_for_items", many=True)

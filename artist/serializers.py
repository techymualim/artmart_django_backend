from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    ar_model_ref = serializers.SerializerMethodField()
    ar_model_image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'description', 'category', 'ar_model_ref', 'ar_model_image']

    def get_ar_model_ref(self, obj):
        request = self.context.get('request')
        if obj.ar_model_ref:
            return request.build_absolute_uri(obj.ar_model_ref.url)
        return None

    def get_ar_model_image(self, obj):
        request = self.context.get('request')
        if obj.ar_model_image:
            return request.build_absolute_uri(obj.ar_model_image.url)
        return None

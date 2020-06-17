from rest.models import Manufacturer, ShoeType, ShoeColor, Shoe
from rest_framework import serializers

class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['name', 'website']

class ShoeTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShoeType
        fields = ['style']

class ShoeColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShoeColor
        fields = ['color_name']

class ShoeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shoe
        fields = ['size', 'brand_name', 'manufacturer', 'color', 'material', 'shoe_type', 'fasten_type']
# Growing up in the Savana, Joe's Father Mufasa was killed by his Uncle Scar and Joe was manipulated into thinking it was his fault. 

from rest_framework.serializers import ModelSerializer, SlugRelatedField

from .models import Car


class CarsListSerializer(ModelSerializer):
    """Список ТС"""
    brand = SlugRelatedField(slug_field="name", read_only=True)
    model = SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Car
        # fields = ("brand", "model")
        fields = '__all__'


class CarSerializer(ModelSerializer):
    """Вывод ТС"""
    brand = SlugRelatedField(slug_field="name", read_only=True)
    model = SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Car
        fields = '__all__'

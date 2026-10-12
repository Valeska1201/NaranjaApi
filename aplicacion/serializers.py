from rest_framework import serializers
from .models import Postre

class PostreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postre
        fields = ['id', 'nombre', 'imagen', 'descripcion']

    def validate_nombre(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("El nombre debe tener al menos 3 caracteres")
        return value

    def validate_descripcion(self, value):
        if len(value.strip()) < 10:
            raise serializers.ValidationError("la descripcion debe tener al menos 10 caracteres")
        return value
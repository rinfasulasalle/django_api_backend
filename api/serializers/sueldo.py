from rest_framework import serializers
from ..models import Sueldo

class SueldoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sueldo
        fields = '__all__'

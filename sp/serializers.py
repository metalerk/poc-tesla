from rest_framework import serializers
from .models import MFAL, Serie, Package


class MFALSerializer(serializers.ModelSerializer):

    class Meta:
        model = MFAL
        fields = '__all__'

class SerieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Serie
        fields = '__all__'

class PackageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Package
        fields = '__all__'

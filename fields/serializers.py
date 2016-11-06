from rest_framework import serializers
from django.contrib.auth.models import User
from fields.models import Field


class FieldSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Field
        fields = ('url', 'id', 'phone', 'field', 'city', 'country', 'temp', 'humidity',
                  'nitrate', 'phosphorus', 'potassium', 'pH', 'light',
                  'envTemp', 'envHumidity', 'precipProb', 'lastUpdate', 'owner')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    fields = serializers.HyperlinkedRelatedField(many=True, view_name='field-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'fields')

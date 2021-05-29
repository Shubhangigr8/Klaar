from django.db.models import fields
from rest_framework import serializers
from api.models import Branches


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = '__all__'
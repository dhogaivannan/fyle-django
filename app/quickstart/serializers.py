from django.contrib.auth.models import User, Group
from rest_framework import serializers
from app.quickstart.models import Branches


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class BranchSerailizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Branches
        fields = ['ifsc', 'bank_id', 'branch', 'address', 'city', 'district', 'state']

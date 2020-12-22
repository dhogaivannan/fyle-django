from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from app.quickstart.serializers import UserSerializer, GroupSerializer, BranchSerailizer
from app.quickstart.models import Branches
from django.contrib.postgres.search import SearchVector


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ApiSet(viewsets.ModelViewSet):
    serializer_class = BranchSerailizer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        query = self.request.query_params.get('q', None)
        # limit = self.request.query_params.get('limit', None)
        # offset = self.request.query_params.get('offset', None)
        return Branches.objects.annotate(
            search=SearchVector('branch')
        ).filter(search=query).order_by('ifsc')


class BranchSet(viewsets.ModelViewSet):
    serializer_class = BranchSerailizer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        query = self.request.query_params.get('q', None)
        # limit = self.request.query_params.get('limit', None)
        # offset = self.request.query_params.get('offset', None)
        return Branches.objects.annotate(
            search=SearchVector('branch') + SearchVector('ifsc') + SearchVector('city') + SearchVector(
                'address') + SearchVector('district') + SearchVector('state')
        ).filter(search=query).order_by('ifsc')

from django.views import generic
from rest_framework import permissions, viewsets
from .permissions import IsOwnerOrReadOnly
from .serializers import *

from .models import CustomUser


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class UserDetailView(generic.DetailView):
    model = CustomUser


class SettingViewSet(viewsets.ModelViewSet):
    queryset = Setting.objects.exclude(deleted_at__isnull=False)
    serializer_class = SettingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class SettingDetailView(generic.DetailView):
    model = Setting


class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.exclude(deleted_at__isnull=False)
    serializer_class = LogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class LogDetailView(generic.DetailView):
    model = Log


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.exclude(deleted_at__isnull=False)
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class CategoryDetailView(generic.DetailView):
    model = Category


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.exclude(deleted_at__isnull=False)
    serializer_class = RegionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class RegionDetailView(generic.DetailView):
    model = Region


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.exclude(deleted_at__isnull=False)
    serializer_class = DistrictSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class DistrictDetailView(generic.DetailView):
    model = District


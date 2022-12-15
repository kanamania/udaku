from datetime import datetime

from django.views import generic
from rest_framework import viewsets, permissions
from .permissions import IsOwnerOrReadOnly
from .serializers import *
from .models import *


class PostCategoryViewSet(viewsets.ModelViewSet):
    queryset = PostCategory.objects.exclude(deleted_at__isnull=False)
    serializer_class = PostCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def perform_delete(self, serializer):
        serializer.save(remover=self.request.user, deleted_at=datetime.now())


class PostCategoryDetailView(generic.DetailView):
    model = PostCategory


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.exclude(deleted_at__isnull=False)
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def perform_update(self, serializer):
        serializer.save(modifier=self.request.user)

    def perform_delete(self, serializer):
        serializer.save(remover=self.request.user, deleted_at=datetime.now())


class PostDetailView(generic.DetailView):
    model = Post


class PostReactionViewSet(viewsets.ModelViewSet):
    queryset = PostReaction.objects.exclude(deleted_at__isnull=False)
    serializer_class = PostReactionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def perform_delete(self, serializer):
        serializer.save(remover=self.request.user, deleted_at=datetime.now())


class PostCommentViewSet(viewsets.ModelViewSet):
    queryset = PostComment.objects.exclude(deleted_at__isnull=False)
    serializer_class = PostCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def perform_delete(self, serializer):
        serializer.save(remover=self.request.user, deleted_at=datetime.now())


class PostCommentDetailView(generic.DetailView):
    model = PostComment


class PostCommentReactionViewSet(viewsets.ModelViewSet):
    queryset = PostCommentReaction.objects.exclude(deleted_at__isnull=False)
    serializer_class = PostCommentReactionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def perform_delete(self, serializer):
        serializer.save(remover=self.request.user, deleted_at=datetime.now())

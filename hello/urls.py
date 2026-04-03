# hello/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, PostViewSet, MediaViewSet,
    FollowViewSet, LikeViewSet, CommentViewSet,
    RefreshTokenViewSet, StoryViewSet, NoteViewSet
)
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'media', MediaViewSet)
router.register(r'follows', FollowViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'refresh_tokens', RefreshTokenViewSet)
router.register(r'stories', StoryViewSet)
router.register(r'notes', NoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


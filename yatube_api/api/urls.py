from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet


router_v1 = DefaultRouter()
router_v1.register(r'posts', PostViewSet, basename='posts')
router_v1.register(r'groups', GroupViewSet, basename='groups')
router_v1.register(r'follow', FollowViewSet, basename='follow')

router_comment_v1 = DefaultRouter()
router_comment_v1.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router_v1.urls)),
    path('posts/<int:post_id>/', include(router_comment_v1.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]

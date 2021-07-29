from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    PostListAPIView,
    PostCreateAPIView,
    PostUpdateAPIView,
    PostDestroyAPIView,
    CommentListAPIView,
    CommentCreateAPIView,
    CommentUpdateAPIView,
    CommentDestroyAPIView,
    UpVotePost,
    SignUpView,
)

urlpatterns = [
    path("posts/", PostListAPIView.as_view(), name="read posts"),
    path("posts/create/", PostCreateAPIView.as_view(), name="create post"),
    path("posts/update/<int:pk>/", PostUpdateAPIView.as_view(), name="update post"),
    path("posts/delete/<int:pk>/", PostDestroyAPIView.as_view(), name="delete post"),
    path("posts/comments/", CommentListAPIView.as_view(), name="read comments"),
    path(
        "posts/comments/create/", CommentCreateAPIView.as_view(), name="create comment"
    ),
    path(
        "posts/comments/update/<int:pk>/",
        CommentUpdateAPIView.as_view(),
        name="update comment",
    ),
    path(
        "posts/comments/delete/<int:pk>/",
        CommentDestroyAPIView.as_view(),
        name="delete comment",
    ),
    path("posts/upvote/", UpVotePost.as_view(), name="create post"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("signup/", SignUpView.as_view(), name="signup"),
]

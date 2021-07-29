from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from .serializers import (
    PostsSerializer,
    SignUpSerializer,
    CommentsSerializer,
    UpVotesSerializer,
)
from .models import Posts, Comments, UpVotes


class PostCreateAPIView(generics.CreateAPIView):
    serializer_class = PostsSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Posts.objects.all()


class PostListAPIView(generics.ListAPIView):
    serializer_class = PostsSerializer
    permission_classes = (AllowAny,)
    queryset = Posts.objects.all()
    filter_backends = [SearchFilter]
    search_fields = [
        "pk",
    ]


class PostUpdateAPIView(generics.UpdateAPIView):
    serializer_class = PostsSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Posts.objects.all()
    lookup_field = "pk"

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        user_is_author = str(instance.author_name) == str(request.user)
        if user_is_author:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response({"message": "failed", "details": serializer.errors})
        else:
            return Response({"message": "failed", "details": "don`t have permission"})


class PostDestroyAPIView(generics.DestroyAPIView):
    serializer_class = PostsSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Posts.objects.all()
    lookup_field = "pk"

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user_is_author = str(instance.author_name) == str(request.user)
        if user_is_author:
            self.perform_destroy(instance)
            return Response({"message": "success", "details": "post deleted"})
        else:
            return Response({"message": "failed", "details": "don`t have permission"})


class CommentCreateAPIView(generics.CreateAPIView):
    serializer_class = CommentsSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Comments.objects.all()


class CommentListAPIView(generics.ListAPIView):
    serializer_class = CommentsSerializer
    permission_classes = (AllowAny,)
    queryset = Comments.objects.all()
    filter_backends = [SearchFilter]
    search_fields = [
        "id",
    ]


class CommentUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CommentsSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Comments.objects.all()
    lookup_field = "pk"

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        user_is_author = str(instance.author_name) == str(request.user)
        if user_is_author:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response({"message": "failed", "details": serializer.errors})
        else:
            return Response({"message": "failed", "details": "don`t have permission"})


class CommentDestroyAPIView(generics.DestroyAPIView):
    serializer_class = CommentsSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Comments.objects.all()
    lookup_field = "pk"

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user_is_author = str(instance.author_name) == str(request.user)
        if user_is_author:
            self.perform_destroy(instance)
            return Response({"message": "success", "details": "post deleted"})
        else:
            return Response({"message": "failed", "details": "don`t have permission"})


class UpVotePost(generics.CreateAPIView):
    serializer_class = UpVotesSerializer
    queryset = UpVotes.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        filters = {
            "author_name": self.request.user,
            "related_post": self.request.data["related_post"],
        }
        post_is_upvoted_by_user = self.get_queryset().filter(**filters).exists()
        if post_is_upvoted_by_user:
            raise ValidationError("post already liked")
        else:
            serializer.save()


class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = SignUpSerializer


def reset_upvotes():
    print("Reseting upvotes")
    UpVotes.objects.all().delete()
    Posts.objects.all().update(amount_of_upvotes=0)

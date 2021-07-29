from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import Posts, Comments, UpVotes


class PostsSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    link = serializers.CharField(required=True)
    creation_date = serializers.DateField(read_only=True)
    amount_of_upvotes = serializers.IntegerField(read_only=True)
    author_name = serializers.CharField(read_only=True)

    def create(self, validated_data):
        return Posts.objects.create(
            **validated_data, author_name=self.context["request"].user
        )

    class Meta:
        model = Posts
        fields = [
            "id",
            "title",
            "link",
            "creation_date",
            "amount_of_upvotes",
            "author_name",
        ]


class CommentsSerializer(serializers.ModelSerializer):
    related_post = serializers.PrimaryKeyRelatedField(
        required=True, queryset=Posts.objects.all()
    )
    content = serializers.CharField(required=True)
    creation_date = serializers.DateField(read_only=True)
    author_name = serializers.CharField(read_only=True)

    def create(self, validated_data):
        return Comments.objects.create(
            **validated_data, author_name=self.context["request"].user
        )

    class Meta:
        model = Comments
        fields = ["id", "related_post", "content", "creation_date", "author_name"]


class UpVotesSerializer(serializers.ModelSerializer):
    related_post = serializers.PrimaryKeyRelatedField(
        required=True, queryset=Posts.objects.all()
    )
    creation_date = serializers.DateField(read_only=True)
    author_name = serializers.CharField(read_only=True)

    def create(self, validated_data):
        upvote = UpVotes.objects.create(
            **validated_data, author_name=self.context["request"].user
        )
        validated_data["related_post"].amount_of_upvotes += 1
        validated_data["related_post"].save()
        return upvote

    class Meta:
        model = UpVotes
        fields = ["id", "related_post", "creation_date", "author_name"]


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("username", "password", "password2", "email")

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user

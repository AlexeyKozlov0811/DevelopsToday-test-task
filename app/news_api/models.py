from django.db import models


# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    link = models.CharField(max_length=255, verbose_name="Link")
    creation_date = models.DateField(auto_now_add=True, verbose_name="Creation Date")
    amount_of_upvotes = models.PositiveIntegerField(
        default=0, verbose_name="Amount of upvotes"
    )
    author_name = models.CharField(max_length=255, verbose_name="Author")


class Comments(models.Model):
    related_post = models.ForeignKey(
        "Posts", on_delete=models.CASCADE, verbose_name="Related post"
    )
    author_name = models.CharField(max_length=255, verbose_name="Author")
    content = models.TextField(verbose_name="Content")
    creation_date = models.DateField(auto_now_add=True, verbose_name="Creation Date")


class UpVotes(models.Model):
    related_post = models.ForeignKey(
        "Posts", on_delete=models.CASCADE, verbose_name="Related post"
    )
    author_name = models.CharField(max_length=255, verbose_name="Author")
    creation_date = models.DateField(auto_now_add=True, verbose_name="Creation Date")

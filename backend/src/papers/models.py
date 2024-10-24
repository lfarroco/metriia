from django.db import models


class Paper(models.Model):
    title = models.CharField(max_length=512)
    abstract = models.TextField()
    url = models.URLField()
    embeddings = models.BinaryField()
    created_date = models.DateTimeField("date published")
    updated_date = models.DateTimeField("date updated")

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    papers = models.ManyToManyField(Paper)
    created_date = models.DateTimeField("date created")
    updated_date = models.DateTimeField("date updated")

    def __str__(self):
        return self.first_name + " " + self.last_name

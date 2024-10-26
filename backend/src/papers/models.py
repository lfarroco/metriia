from django.db import models


class Journal(models.Model):
    name = models.CharField(max_length=128)
    embeddings = models.BinaryField(null=True)
    created_date = models.DateTimeField("record date created")
    updated_date = models.DateTimeField("record date updated")

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    embeddings = models.BinaryField(null=True)
    created_date = models.DateTimeField("record date created")
    updated_date = models.DateTimeField("record date updated")

    def __str__(self):
        return self.first_name + " " + self.last_name


class Paper(models.Model):
    title = models.CharField(max_length=512)
    doi = models.CharField(max_length=128, null=True)
    abstract = models.TextField()
    url = models.URLField(null=True)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE, null=True)
    authors = models.ManyToManyField(Author)
    embeddings = models.BinaryField()
    published_date = models.DateTimeField("paper date published")
    created_date = models.DateTimeField("record date published")
    updated_date = models.DateTimeField("record date updated")

    def __str__(self):
        return self.title


class PaperDistance(models.Model):
    paper1 = models.ForeignKey(
        Paper, on_delete=models.CASCADE,
        related_name='paper_distances_as_paper1')
    paper2 = models.ForeignKey(
        Paper, on_delete=models.CASCADE,
        related_name='paper_distances_as_paper2')
    distance = models.FloatField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['paper1', 'paper2'],
                name='unique_paper_pair',
            ),
            models.UniqueConstraint(
                fields=['paper2', 'paper1'],
                name='unique_reverse_paper_pair',
            )
        ]

    created_date = models.DateTimeField("record date created")
    updated_date = models.DateTimeField("record date updated")

    def __str__(self):
        return f'{self.paper1} - {self.paper2} ({self.distance})'

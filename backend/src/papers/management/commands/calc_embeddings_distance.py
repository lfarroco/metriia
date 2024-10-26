from django.core.management.base import BaseCommand
from papers.models import Paper, Journal, Author, PaperDistance
import json
from django.utils import timezone
import requests


class Command(BaseCommand):
    help = 'This command calculates the distance between each pair of papers'

    def handle(self, *args, **kwargs):

        papers = Paper.objects.all()

        print(f'Papers: {len(papers)}')

        for i, paper1 in enumerate(papers):

            print(f'Processing paper {i + 1} of {len(papers)}')

            for j, paper2 in enumerate(papers):

                if i >= j:
                    continue

                print(f'Processing paper {i + 1} of {len(papers)}')

                embeddings_1 = json.loads(
                    paper1.embeddings.decode('utf-8'))
                embeddings_2 = json.loads(
                    paper2.embeddings.decode('utf-8'))

                dot_product = sum(
                    a * b for a, b in zip(embeddings_1, embeddings_2))

                magnitude_1 = sum(a ** 2 for a in embeddings_1) ** 0.5
                magnitude_2 = sum(b ** 2 for b in embeddings_2) ** 0.5

                cosine_similarity = dot_product / (magnitude_1 * magnitude_2)

                PaperDistance.objects.create(
                    paper1=paper1,
                    paper2=paper2,
                    distance=cosine_similarity,
                    created_date=timezone.now(),
                    updated_date=timezone.now()
                )

        self.stdout.write(self.style.SUCCESS('Task completed!'))

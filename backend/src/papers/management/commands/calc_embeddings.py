from django.core.management.base import BaseCommand
from papers.models import Paper, Journal, Author
import json
from django.utils import timezone
import requests


class Command(BaseCommand):
    help = 'This command generated embeddings based on the abstracts of the papers'

    def handle(self, *args, **kwargs):

        print('Generating embeddings...')

        papers = Paper.objects.all(
        )

        print(f'Papers without embeddings: {len(papers)}')

        for i, paper in enumerate(papers):

            print(f'Processing paper {
                  i + 1} of {len(papers)}')

            # curl http://localhost:11434/api/embeddings -d '{
            #   "model": "mxbai-embed-large",
            #   "prompt": "Llamas are members of the camelid family"
            # }'
            req = requests.post('http://host.docker.internal:11434/api/embeddings', json={
                'model': 'mxbai-embed-large',
                'prompt': f"{paper.title} - {paper.abstract}"
            })

            embeddings = req.json()['embedding']

            embeddings_bytes = json.dumps(embeddings).encode('utf-8')

            paper.embeddings = embeddings_bytes
            paper.save()

        self.stdout.write(self.style.SUCCESS('Task completed!'))

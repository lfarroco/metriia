from django.core.management.base import BaseCommand
from papers.models import Paper, Journal, Author
import json
from django.utils import timezone
import datetime


class Command(BaseCommand):
    help = 'Describe what your custom command does'

    def add_arguments(self, parser):
        # Add any arguments you need for your task
        parser.add_argument('param', type=str, help='A parameter for the task')

    def handle(self, *args, **kwargs):
        param = kwargs['param']
        self.stdout.write(self.style.SUCCESS(
            f'Starting task with param: {param}'))

        # Perform your task here
        # For example, updating some models
        print('Updating models...')

        with open('/usr/src/app/src/papers/arxiv.json', 'r') as file:

            i = 1
            for line in file:
                json_obj = json.loads(line)

                is_cs = json_obj['categories'].find('cs.SE') != -1
                if not is_cs:
                    continue

                # Example json_obj:
                # {
                # 'id': '0704.0012',
                #  'submitter': 'Dohoon Choi',
                #  'authors': 'Dohoon Choi',
                #  'title': 'Distribution of... ',
                #  'comments': None,
                #  'journal-ref': None,
                #  'doi': None,
                #  'report-no': None,
                #  'categories': 'math.NT',
                #  'license': None,
                #  'abstract': "  Recently... ",
                #  'versions': [{'version': 'v1', 'created': 'Sat, 31 Mar 2007 05:48:51 GMT'}],
                #  'update_date': '2007-05-23',
                #  'authors_parsed': [['Choi', 'Dohoon', '']]
                # }

                journal = None
                if json_obj['journal-ref'] is not None:
                    journal, _ = Journal.objects.get_or_create(
                        name=json_obj['journal-ref'],
                        created_date=timezone.now(),
                        updated_date=timezone.now()
                    )

                for author in json_obj['authors_parsed']:
                    author, _ = Author.objects.get_or_create(
                        first_name=author[1],
                        last_name=author[0],
                        created_date=timezone.now(),
                        updated_date=timezone.now()
                    )

                paper = Paper.objects.create(
                    title=json_obj['title'],
                    doi=json_obj['doi'],
                    abstract=json_obj['abstract'],
                    url=f'https://arxiv.org/abs/{json_obj["id"]}',
                    # use date from 1st version
                    published_date=datetime.datetime.strptime(
                        json_obj['versions'][0]['created'], '%a, %d %b %Y %H:%M:%S %Z'),
                    created_date=timezone.now(),
                    updated_date=timezone.now()
                )

                if journal is not None:
                    paper.journal = journal
                    paper.save()

                i += 1
                if i > 100:
                    break

        self.stdout.write(self.style.SUCCESS('Task completed!'))

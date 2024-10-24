
from papers.models import Paper
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


def detail(request, paper_id):
    paper = get_object_or_404(Paper, pk=paper_id)
    return JsonResponse({
        'title': paper.title,
        'abstract': paper.abstract,
        'url': paper.url,
    })


def list(request):
    papers = Paper.objects.all()
    return JsonResponse({
        'papers': [
            {
                'id': paper.id,
                'title': paper.title,
                'abstract': paper.abstract,
                'url': paper.url,
            }
            for paper in papers
        ]
    })

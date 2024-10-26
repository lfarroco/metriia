
from django.db.models import Q
from papers.models import Paper, PaperDistance
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


def detail(request, paper_id):
    paper = get_object_or_404(Paper, pk=paper_id)

    distances = []
    distances_query_set = PaperDistance.objects.filter(
        Q(paper1__id=paper_id) | Q(paper2__id=paper_id)
    ).order_by(
        'distance')

    def paper_dict(id, title):
        return {
            'id': id,
            'title': title
        }

    for distance in distances_query_set:
        # filter self
        if distance.paper1.id == paper_id:
            distances.append(paper_dict(
                distance.paper2.id, distance.paper2.title))
        else:
            distances.append(paper_dict(
                distance.paper1.id, distance.paper1.title))

    distances = distances[:5]

    return JsonResponse({
        'title': paper.title,
        'abstract': paper.abstract,
        'url': paper.url,
        'similar': distances
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

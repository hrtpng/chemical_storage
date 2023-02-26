from django.views import View
from django.http import HttpResponse
from storage.models import Compound
from django.db.models import Q
import json


class StorageView(View):
    def get(self, request):
        search = request.GET.get("search")
        print(search)
        compounds = Compound.objects.all().filter(
            Q(title__contains=search)
            | Q(formula__contains=search)
            | Q(iupac__contains=search)
            | Q(cas__contains=search)
            | Q(tags__contains=search)
        )
        data = []
        for comp in compounds:
            data.append(
                {
                    "title": comp.title,
                    "formula": comp.formula,
                    "cas": comp.cas,
                    "rack": comp.rack,
                    "shelf": comp.shelf,
                }
            )
        return HttpResponse(json.dumps(data), content_type="application/json")

    def post(self, request):
        ...

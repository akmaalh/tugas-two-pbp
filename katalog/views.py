from django.shortcuts import render
from katalog.models import CatalogItem
# TODO: Create your views here.
def show_katalog(request):
    data_katalog = CatalogItem.objects.all()
    context = {
        'list_katalog': data_katalog,
        'name': 'Muhammad Akmal Hakim',
        'id': '2106750383',
    }
    return render(request, "katalog.html", context)
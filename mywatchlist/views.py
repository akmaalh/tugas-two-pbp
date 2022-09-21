from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import MyWatchlist
# Create your views here.
def show_watchlist_index(request):
    watchlist = MyWatchlist.objects.all()
    watched_count = 0
    unwathched_count = 0
    res = False
    
    for item in watchlist:
        if item.watched:
            watched_count += 1
        else:
            unwathched_count += 1
    if watched_count > unwathched_count:
        res = True
    
    context = {
        'is_watched_more': res,
    }
    
    return render(request, 'watchlist_bonus.html', context)

def show_watchlist(request):
    watchlist = MyWatchlist.objects.all()
    context = {
        'watchlist': watchlist,
        'nama' : 'Muhammad Akmal Hakim',
        'id' : '2106750383'
    }
    return render(request, 'watchlist.html', context)

def show_xml(request):
    data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')
def show_json(request):
    data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')
def show_html(request):
    data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize('html', data), content_type='application/html')
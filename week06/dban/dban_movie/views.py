from django.shortcuts import render, HttpResponse, get_list_or_404
from .models import MovieComment
import json

# Create your views here.

def index(request):
    all_comments = MovieComment.objects.filter(n_star__gt=3)
    return render(request, 'index.html', locals())

def filter(request):
    filter_str = request.GET.get('q')
    #all_comments = MovieComment.objects.filter(short_comment__icontains=filter_str)
    all_comments = get_list_or_404(MovieComment,short_comment__icontains=filter_str)
    return render(request, 'index.html', locals())
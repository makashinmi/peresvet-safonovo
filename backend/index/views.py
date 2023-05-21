from django.shortcuts import render
from django.http import HttpRequest as rq, HttpResponse as rp

from .models import *

# Create your views here.
def index(request: rq):
    

    context = {
        'slider_list': [],
        'trainer_list': Trainer.objects.all(),
        'post_list': Post.objects.all()[:3],
        'photo_list': Photo.objects.all()[:9],
    }

    return render(request, 'index.html', context)

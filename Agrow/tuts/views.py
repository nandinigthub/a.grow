from django.shortcuts import render
from .models import Video

# Create your views here.
def videos(request):
    videos = Video.objects.all()
    return render(request,'tuts/tuts.html', context= {'videos': videos})

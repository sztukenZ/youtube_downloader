from django.shortcuts import render, redirect
from pytube import YouTube

# Create your views here.
def youtube(request):
    if request.method == "POST":
        print(f"HERE {request}")
        link = request.POST['link']
        print(link)
        video = YouTube(link)

        stream = video.streams.get_lowest_resolution()

        stream.download()
        return render(request, 'downloader/index.html', context_instance = RequestContext(request))
    return render(request, 'downloader/index.html', context_instance = RequestContext(request))
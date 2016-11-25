from django.shortcuts import render
from videos.models import Video

#def hello(request):
#    return HttpResponse("Hello world")

def video(request, video_name):
    print video_name
    v = Video.objects.get(name=video_name)
    i = v.views + 1
    v.views = i
    v.save()
    #rv = Video.objects.order_by("time")[:10]
    #pv = video.objects.order_by("views")[0:10]
    c = {"main_video": v}
        # "recent_videos": rv,
        # "popular_videos": pv}
    return render(request, 'index.html', c)

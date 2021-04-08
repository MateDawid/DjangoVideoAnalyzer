from django.shortcuts import render
from django.views.decorators import gzip
from django.views.generic import CreateView
from django.http import StreamingHttpResponse
from videoanalyzer.video import VideoCamera, gen

from .models import DisplayModel
from .forms import DisplayForm


class CreateDisplayView(CreateView):
    model = DisplayModel
    form_class = DisplayForm
    template_name = 'templates/main/base.html'
    # success_url = 'myapp/success.html'

@gzip.gzip_page
def clean_feed(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        pass

# @gzip.gzip_page
# def shape_feed(request):
#     try:
#         cam = VideoCamera()
#         return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
#     except:  # This is bad! replace it with proper handling
#         pass
#
# @gzip.gzip_page
# def color_feed(request):
#     try:
#         cam = VideoCamera()
#         return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
#     except:  # This is bad! replace it with proper handling
#         pass
#
# @gzip.gzip_page
# def face_feed(request):
#     try:
#         cam = VideoCamera()
#         return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
#     except:  # This is bad! replace it with proper handling
#         pass

def home(request):
    form = DisplayForm(request.POST or None, request.FILES or None)
    return render(request, "main/base.html", {"form": form})


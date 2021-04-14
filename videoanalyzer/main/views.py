from django.shortcuts import render
from django.views.decorators import gzip
from django.views.generic import CreateView
from django.http import StreamingHttpResponse
from videoanalyzer.video import VideoCamera, gen

# from .models import DisplayModel
from .forms import CircleDetectionForm

@gzip.gzip_page
def feed(request):
    if dict(request.session) != {}:
        if request.session['circle_detection'] != {}:
            try:
                print(dict(request.session))
                data = request.session['circle_detection']
                cam = VideoCamera(shapeDetection="circle",
                                  dp=float(data['dp']),
                                  minDist=float(data['minDist']),
                                  param1=float(data['param1']),
                                  param2=float(data['param2']),
                                  minRadius=int(data['minRadius']),
                                  maxRadius=int(data['maxRadius']))
                del request.session['circle_detection']
                return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
            except:  # This is bad! replace it with proper handling
                pass
    else:
        try:
            print(dict(request.session))
            cam = VideoCamera(shapeDetection="triangle")
            return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
        except:  # This is bad! replace it with proper handling
            pass


def home(request):
    return render(request, "main/index.html")


def shape(request):
    return render(request, "main/shape.html")


def detect_circle(request):
    circle_form = CircleDetectionForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        request.session["circle_detection"] = request.POST
    else:
        request.session["circle_detection"] = {}
    return render(request, "main/circle.html", {"circle_form": circle_form})

def detect_triangle(request):
    # triangle_form = TriangleDetectionForm(request.POST or None, request.FILES or None)
    # if request.method == 'POST':
    #     request.session["triangle_detection"] = request.POST
    # else:
    #     request.session["triangle_detection"] = {}
    return render(request, "main/triangle.html")  # ,{"triangle_form": triangle_form})

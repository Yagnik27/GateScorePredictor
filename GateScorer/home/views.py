from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'home/homepage.html')

def home_index(request):
    return render(request,'home/home_index.html')

def quizz_index(request):
    return render(request,'quiz/base.html')

def about(request):
    return render(request,'home/about.html')
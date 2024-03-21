
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Movie
from .forms import MovieForm
# Create your views here.
def index(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie
    }
    return render(request,'index.html',context)
def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render (request,"detail.html",{'movie':movie})
def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc=request.POST.get('desc',)
        img=request.FILES['img']
        actors=request.POST.get('actors',)
        release_date=request.POST.get('release_date',)
        category=request.POST.get('category',)
        movie=Movie(name=name,desc=desc,img=img,actors=actors,release_date=release_date,category=category)
        movie.save()
        return redirect('/')
    return render(request, 'add.html')

def add_movi(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc=request.POST.get('desc',)
        img = request.FILES['img']
        actors = request.POST.get('actors', )
        release_date = request.POST.get('release_date', )
        category = request.POST.get('category', )
        movie = Movie(name=name, desc=desc, img=img, actors=actors, release_date=release_date, category=category)
        movie.save()
    return render(request, 'index.html')

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')

def Review(request):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'Review.html')

##############login and registration#############



from django.shortcuts import render, get_object_or_404, redirect
from .models import home_db
from django.utils import timezone

# Create your views here.

def home(request):
    homes = home_db.objects.all()
    return render(request, 'home.html', {'homes' : homes})

def detail(request, home_id):
    home_detail = get_object_or_404(home_db, pk=home_id)
    return render(request, 'detail.html', {'home' : home_detail})

def about(request):
    return render(request, 'about.html')

def result(request):
    full = request.GET['fulltext']
    words = full.split()
    words_dic = {}
    for word in words:
        if word in words_dic:
            words_dic[word] += 1
        else:
            words_dic[word] = 1
    return render(request, 'result.html', {'full':full, 'length':len(words), 'dic': words_dic.items() })

def new(request):
    return render(request, 'new.html')

def create(request):
    home = home_db()
    home.title = request.GET['title']
    home.body = request.GET['body']
    home.pub_date = timezone.datetime.now()
    home.save()
    return redirect('/home/'+str(home.id))
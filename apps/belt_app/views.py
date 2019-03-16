from django.shortcuts import render, HttpResponse, redirect
from . models import *
from django.contrib import messages
from django.contrib.auth import logout
from time import gmtime, strftime
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'belt_app/index.html')

def login(request):#LOGIN   
    result = User.objects.log_validator(request.POST)
    if len(result) > 0:
        for key in result.keys():
            messages.error(request, result[key])
        return redirect('/')
    else:
        user = User.objects.get(email = request.POST['log_email'])
        request.session['user_id'] = user.id      
    return redirect('/ideas')

def create(request):#REG new user
    result = User.objects.reg_validator(request.POST)
    if len(result) > 0:
        for key in result.keys():
            messages.error(request, result[key])
        return redirect('/') 
    else:
        hashedpw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = hashedpw)
        user = User.objects.last()
        request.session['user_id'] = user.id
    return redirect('/ideas')

def ideas(request):
    context = {
        'ideas' : Idea.objects.all(),
        'user' : User.objects.get(id = request.session['user_id']),      
    }
    return render(request, 'belt_app/ideas.html', context)

def new(request):

    return render(request, 'belt_app/new.html')
    
def add(request):
    result = User.objects.validator(request.POST)
    if len(result) > 0:
        for key in result.keys():
            messages.error(request, result[key])
        return redirect('/new') 
    else: 
        if request.method == "POST":
            idea = Idea.objects.create(context = request.POST['context'], posted_id= request.session['user_id'])
            return redirect("/ideas")
        else:
            return redirect("/ideas")  

def view(request, id):
    idea = Idea.objects.get(id = id)
    time = strftime("%b %d, %Y", gmtime())
    context = {
        'idea' : idea,
        'time' : time,
    }
    return render(request, 'belt_app/view.html', context)  

def edit(request, id):
    idea = Idea.objects.get(id = id)
    context = {
        'idea' : idea,
    }
    return render(request, 'belt_app/edit.html', context)  

def update(request, id):
    x = id 
    result = User.objects.validator(request.POST)
    if len(result) > 0:
        for key in result.keys():
            messages.error(request, result[key])
        return redirect('/edit/'+ str(x)) 
    else:
        b = Idea.objects.get(id=id)
        b.context = request.POST['title']
        b.save()
    return redirect('/ideas')  

def delete(request, idea_id):
    Idea.objects.get(id= idea_id).delete()
    return redirect('/ideas')

def logout_user(request):
    request.session.flush()
    return redirect('/')    
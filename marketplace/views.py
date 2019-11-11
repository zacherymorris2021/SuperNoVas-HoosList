from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Item, Seller, Message
from .myForms import ItemAddForm, SendMessageForm
from django.contrib.auth.models import User

# views
@login_required(login_url='home')
def index(request):
    latest_item_list = Item.objects.order_by('-item_add_date')
    template = loader.get_template('marketplace/index.html')
    context={
        'latest_item_list': latest_item_list,
    }
    return render(request, 'marketplace/index.html', context)

@login_required(login_url='home')
def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'marketplace/detail.html', {'item':item})

@login_required(login_url='home')
def add_item(request):
    if request.method == "POST":
        form = ItemAddForm(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.seller = request.user
            new_item.save()
            return redirect('/marketplace')
    else:
        form = ItemAddForm()
    return render(request, 'marketplace/add-item.html', {'form': form})

@login_required(login_url='home')
def map(request):
    item_list = Item.objects.order_by('-item_add_date')
    context={
        'item_list': item_list,
    }
    return render(request, 'marketplace/map.html', context)

def search(request):
    template = 'marketplace/search.html'
    query = request.GET.get('q')
    if query:
        results = Item.objects.filter(Q(item_name__icontains=query) | Q(item_description__icontains = query) | Q(item_categories__icontains = query))
    else:
        results = "No items found"
    context = {
        'results' : results
    }
    return render(request, template, context)

@login_required(login_url='home')
def logout_user(request):   
    logout(request)
    return redirect('home')

@login_required(login_url='home')
def profile(request):
    return render(request, 'marketplace/profile.html', {})
@login_required(login_url='home')
def user(request, user_id ):
    seller = get_object_or_404(User, pk=request.user.id)
    return render(request, 'marketplace/user.html',{'seller':seller})

@login_required(login_url='home')
def filter(request):
    template = 'marketplace/filter.html'
    query = request.GET.get('f')
    if query:
        filters = Item.objects.filter(Q(item_categories__contains=query))
    else:
        filters = "No items found"
    context = {
        'filters' : filters
    }
    return render(request, template, context)

@login_required(login_url='home')
def inbox(request):
    context = {
        'messages': Message.objects.filter(receiver=request.user)
    }
    return render(request, 'marketplace/inbox.html', context)

@login_required(login_url='home')
def message(request):
    if request.method == "POST":
        form = SendMessageForm(request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            message.seller = request.user
            new_item.save()
            return redirect('/marketplace')
    else:
        form = SendMessageForm()
    return render(request, 'marketplace/message.html', {'form': form})
    #return HttpResponseRedirect()

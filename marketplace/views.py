from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Item, Seller, Message
from .myForms import ItemAddForm, SendMessageForm, SendReplyForm, UserRatingForm
from django.contrib.auth.models import User
from .filters import ItemFilter
from django.contrib import messages

# views
def index(request):
    latest_item_list = Item.objects.order_by('-item_add_date')
    template = loader.get_template('marketplace/index.html')
    context={
        'latest_item_list': latest_item_list,
    }
    return render(request, 'marketplace/index.html', context)

def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'marketplace/detail.html', {'item':item})

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

def logout_user(request):
    logout(request)
    return redirect('home')

def profile(request):
    return render(request, 'marketplace/profile.html', {})

def delete(request, item_id):
    item=get_object_or_404(Item, pk=item_id)
    creator=item.seller.username
    if request.method=="POST" and request.user.is_authenticated and request.user.username==creator:
        item.delete()
        return HttpResponseRedirect(reverse('marketplace:profile'))
    context={'item': item,
            'creator': creator,
            }
    return render(request, 'marketplace/delete.html', context)


def markSold(request, item_id):
    item=get_object_or_404(Item, pk=item_id)
    creator=item.seller.username
    if request.method=="POST" and request.user.is_authenticated and request.user.username==creator:
        item.item_sold=True
        item.save()
        return HttpResponseRedirect(reverse('marketplace:profile'))
    context={'item': item,
            'creator': creator,
            }
    return render(request, 'marketplace/markSold.html', context)

def user(request, seller_id ):
    seller = get_object_or_404(User, pk=seller_id)
    form = UserRatingForm()
    return render(request, 'marketplace/user.html',{'seller':seller, 'form':form})

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

def inbox(request):
    context = {
        'messages': Message.objects.filter(receiver_id=request.user.id).order_by('-timesent')
    }
    return render(request, 'marketplace/inbox.html', context)

def outbox(request):
    context = {
        'messages': Message.objects.filter(sender_id=request.user.id).order_by('-timesent')
    }
    return render(request, 'marketplace/outbox.html', context)

def message(request):
    if request.method == "POST":
        form = SendMessageForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.sender = request.user
            new_message.save()
            return redirect('marketplace:inbox')
    else:
        form = SendMessageForm()
        #code inspired from https://djangosnippets.org/snippets/1810/
        for key in request.GET:
            try:
                form.fields[key].initial = request.GET[key]
            except KeyError:
                pass
        # end of inspired code
    context = {
    'form': form
    }
    return render(request, 'marketplace/message.html', context)

def reply(request, message_id):

    ogMessage = get_object_or_404(Message, id=message_id)
    if request.method == "POST":
        form = SendReplyForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.sender = request.user
            new_message.receiver = ogMessage.sender
            new_message.subject = "RE: " + ogMessage.subject
            new_message.save()
            return redirect('marketplace:inbox')
    else:
        form = SendReplyForm()
    context = {
        'form' : form,
        'message' : ogMessage
    }
    return render(request, 'marketplace/reply.html', context)

def advFilter(request):
    item_list = Item.objects.all()
    item_filter = ItemFilter(request.GET, queryset=item_list)
    return render(request, 'marketplace/item_list.html', {'filter': item_filter})

def userRating(request):
    form=UserRatingForm()
    return render(request, 'marketplace/user.html', {'form': form})

def thank(request):
    if request.method == "POST":
        review = request.POST.get('question')
        seller = request.POST.get('user')
        print(review )
        print(seller)
        print(request.user)

        # seller_list = Item.objects.all()

        # search = get_object_or_404(Seller, id=seller)
        #sellerSearch = get_object_or_404(User, id=seller)
        #print(sellerSearch)

        #if(review == 'positive'):
        #    seller.Seller.posRate += 1
        #    print(seller.Seller.posRate)
        #else:
        #    seller.negRate -= 1


    return render(request, 'marketplace/thank.html')

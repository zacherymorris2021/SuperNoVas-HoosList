from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.db.models import Q
from .models import Item, Seller
from .myForms import ItemAddForm

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
        form = ItemAddForm(request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.save()
            return redirect('/marketplace')
    else:
        form = ItemAddForm()
    return render(request, 'marketplace/add-item.html', {'form': form})


def search(request):
    template = 'marketplace/search.html'
    query = request.GET.get('q')
    if query:
        results = Item.objects.filter(Q(item_name__icontains=query) | Q(item_description__icontains = query))
    else:
        results = Item.objects.filter(status="Published")
    context = {
        'results' : results
    }
    return render(request, template, context)

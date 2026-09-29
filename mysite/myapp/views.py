from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
import logging
from django.shortcuts import get_object_or_404
from django.utils import timezone
# Create your views here.
logger = logging.getLogger(__name__)

# cache the page upto this time in seconds
# @cache_page(60 * 15)
# @vary_on_headers("User-Agent")
@login_required 
def index(request):
    logger.info("Fetching all items from the database")
    logger.info(f"User [{timezone.now().isoformat()}] {request.user} request item list from {request.META.get('REMOTE_ADDR')}")
    #fetches all items from the Item database
    item_list = Item.objects.all()
    logger.debug(f"Found {item_list.count()} items")
    
    #initializes django's paginator class
    paginator  = Paginator(item_list, 5)
    
    # capturer's the requested page number from the request
    page_number = request.GET.get("page")
    
    # it takes the page number and returns only 5 item that is on that page
    page_obj = paginator.get_page(page_number)
    
    # passing page_obj to template 
    context = {
        'page_obj': page_obj
    }
    return render(request, 'myapp/index.html', context)

# class IndexClassView(ListView):
#     model = Item
#     template_name = 'myapp/index.html'
#     context_object_name = 'item_list'
    

def item(request):
    return HttpResponse("This is an item.")

def detail(request, id):
    logger.info(f"Fetching an item with id:{id}")
    try:
        item = get_object_or_404(Item, pk=id)
        # item = Item.objects.get(id=id)
        logger.debug(f"Item found {item.item_name} (${item.item_price})")
    except Exception as e:
        logger.error(f"Error fetching the item %s: %s", id, e)
        raise
    
    context = {
        'item': item
    }
    
    return render(request, 'myapp/detail.html', context)


# class FoodDetail(DetailView):
#     model = Item
#     template_name = 'myapp/detail.html'
#     context_object_name = 'item'

def createItem(request):
    form = ItemForm(request.POST or None)
    
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('myapp:index')

    context = {
        'form': form
    }
    
    return render(request, 'myapp/item-form.html', context)

# class ItemCreateView(CreateView):
#     model = Item
#     fields = ['item_name', 'item_description', 'item_price', 'item_image']
#     def form_valid(self, form):
#         form.instance.user_name = self.request.user 
#         return super().form_valid(form)
        
def update_item(request, id):
    item = Item.objects.get(id =id)
    
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('myapp:index')
    
    context = {
        'form': form
    }
    return render(request, 'myapp/item-form.html', context)

class ItemUpdateView(UpdateView):
    model = Item
    fields = ['item_name', 'item_description', 'item_price', 'item_image']
    template_name_suffix = '_update_form'
    
    def get_queryset(self):
        return Item.objects.filter(user_name = self.request.user)
    

def delete_item(request, id):
    item = Item.objects.get(id=id)
    
    if (request.method == "POST"):
        item.delete()
        return redirect('myapp/index')
    return render(request, 'myapp/item-delete.html')

class ItemDelete(DeleteView):
    model = Item
    success_url = reverse_lazy("myapp:index")
    
def get_objects(request):
    for item in Item.objects.all():
        print(item.item_name)
           
def get_objects_optimized(request):
    items = Item.objects.only('item_name')
    for item in items:
        print(item.item_name)
        
        
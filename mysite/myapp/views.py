from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

# @login_required
# def index(request):
#     item_list = Item.objects.all()
#     context = {
#         'item_list': item_list
#     }
    
#     return render(request, 'myapp/index.html', context)

class IndexClassView(ListView):
    model = Item
    template_name = 'myapp/index.html'
    context_object_name = 'item_list'
    

def item(request):
    return HttpResponse("This is an item.")

# def detail(request, id):
#     item = Item.objects.get(id=id)
#     context = {
#         'item': item
#     }
    
#     return render(request, 'myapp/detail.html', context)

class FoodDetail(DetailView):
    model = Item
    template_name = 'myapp/detail.html'
    context_object_name = 'item'

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

class ItemCreateView(CreateView):
    model = Item
    fields = ['item_name', 'item_description', 'item_price', 'item_image']
    def form_valid(self, form):
        form.instance.user_name = self.request.user 
        return super().form_valid(form)
        
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
    

def delete_item(request, id):
    item = Item.objects.get(id=id)
    
    if (request.method == "POST"):
        item.delete()
        return redirect('myapp/index')
    return render(request, 'myapp/item-delete.html')

class ItemDelete(DeleteView):
    model = Item
    success_url = reverse_lazy("myapp:index")
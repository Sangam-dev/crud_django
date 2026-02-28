from django.shortcuts import render, redirect, get_object_or_404
from .models import GroceryItem


def index(request):
    items = GroceryItem.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'index.html', context)


def toggle_completed(request, item_id):

    if request.method == 'POST':
        item = get_object_or_404(GroceryItem, id=item_id)
        item.completed = not item.completed
        item.save()

    return redirect('grocerryapp:index')

# ....

def delete_item(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(GroceryItem, id=item_id)
        item.delete()

    return redirect('grocerryapp:index')

def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            GroceryItem.objects.create(name=name)
    return redirect('grocerryapp:index')

def edit_item(request, item_id):
    item = get_object_or_404(GroceryItem, id=item_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            item.name = name
            item.save()
            return redirect('grocerryapp:index')
    return render(request, 'edit.html', {'item': item})
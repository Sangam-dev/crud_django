from django.shortcuts import render
from .models import GroceryItem


def index(request):
    """Display all grocery items"""
    items = GroceryItem.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'index.html', context)
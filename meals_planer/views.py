from django.shortcuts import render

# Create your views here.
def index(request):
    """The home page for the meal planer"""
    return render(request, 'meals_planer/index.html')

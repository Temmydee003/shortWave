from django.shortcuts import render, redirect
import uuid
from .models import LinkInfo
from django.http import HttpResponse
from django.shortcuts import get_object_or_404 
from django.http import JsonResponse    
from django.db import IntegrityError


def index(request):
    return render(request, 'index.html', {})

def add(request):
    if request.method == 'POST':
        link = request.POST.get('link') # getting the input link
        if not link:
            return JsonResponse({'error': 'URL is Required'}, status=400)
        
        if not link.startswith(('http://', 'https://')):
            link = 'http://' + link

        try:
            link_id = str(uuid.uuid4())[:5] # generating 5 random strings
            LinkInfo.objects.create(link=link, link_id=link_id) # assigning the link and id
            return JsonResponse({'shortcode': link_id})
        except IntegrityError:
            return JsonResponse({'error': 'Failed to generate unquie short URL'}, status=500)
        
    return JsonResponse({'error': 'Invaild request method'}, status=400)

def shorten(request, pk):
    link_obj = get_object_or_404(LinkInfo, link_id = pk)
    return redirect(link_obj.link)
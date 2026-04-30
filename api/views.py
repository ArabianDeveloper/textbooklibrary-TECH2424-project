from django.shortcuts import render
import requests as req
# Create your views here.

def joke(request):
    try:
        types = req.get('https://official-joke-api.appspot.com/types').json()
    except:
        types = []

    if request.method == 'GET':
        try:
            joke = req.get('https://official-joke-api.appspot.com/random_joke').json()
            if request.GET.get('type') != 'random':
                joke = req.get(f'https://official-joke-api.appspot.com/jokes/{request.GET.get("type")}/random').json()[0]
            return render(request, 'api/joke.html', {'joke': joke, 'types': types})
        except Exception as e:
            return render(request, 'api/joke.html', {'joke': e, 'types': types})
    return render(request, 'api/joke.html', {'types': types})
from urllib import response
from django.shortcuts import render
import requests

def index(request):
    url = 'https://fish-text.ru/get?number=5'
    response = requests.get(url).json()
    text = response['text']
    return render(request, 'index.html', context={'word': text})
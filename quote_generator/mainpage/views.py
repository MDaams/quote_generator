from django.shortcuts import render
import requests
import json

# Create your views here.
def main_page(request):
    response = requests.get('http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1')
    payload = json.loads(response.text)
    quote_data = {"quote": payload[0]['content'], "author": payload[0]['title']}
    return render(request, 'main.html', quote_data)

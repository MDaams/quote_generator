from django.shortcuts import render

# Create your views here.
def main_page(request):
    quote = "this is a quote"
    quote_data = {"quote": quote}
    return render(request, 'main.html', quote_data)

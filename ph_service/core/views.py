from django.shortcuts import render
from django.http import HttpResponseForbidden, HttpResponseNotFound
# Create your views here.

def index(request):
	return render(request, 'index.html', {})

def return_word(request):
	word = None
	if request.method == 'POST':
		word = request.POST['word'][::-1]
	return render(request, 'return_word.html', {'word' : word})

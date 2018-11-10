from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
	try: 
		request.session['word']
	except KeyError as e:
		print(e)
		request.session['word'] = ""

	try:
		request.session['counter']
	except KeyError as e:
		print(e)
		request.session['counter'] = 0

	word = {
		'word' : request.session['word'],
		'counter': request.session['counter']
		}

	return render(request, "myapps/index.html", word)

def randomString(request):
	request.session['counter'] += 1
	request.session['word'] = get_random_string(length=14)
	return redirect('/')


def reset(request):
	del request.session['word']
	del request.session['counter']
	return redirect('/')

# Create your views here.

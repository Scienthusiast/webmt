from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def index(request):
	special_training_list = ["Digits", "Cards", "Spoken Numbers"]
	test_yourself_test_list = ["Digits", "Binaries", "Words", "Historical Dates", "Speed Cards", "Cards", "Abstract Images", "Names and Faces"]

	logged_user = {
		'name': "John Doe"
	}

	template = loader.get_template('home/index.html')

	context = {
		'special_training_list': special_training_list,
		'test_yourself_test_list': test_yourself_test_list,
		'logged_user': logged_user
	}

	return HttpResponse(template.render(context, request))



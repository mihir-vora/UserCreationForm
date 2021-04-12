# using django Authentication System

from django.shortcuts import render

# Create your views here.
def signUp(request):
	if request.method == "POST":
		form =  userCreationForm()
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

class Home(View):

	def get(self, request, *args, **kwargs):
		return render(request, 'home.html')
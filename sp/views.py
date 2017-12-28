from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

class SP(View):

	def get(self, request, *args, **kwargs):
		return render(request, 'sp.html')
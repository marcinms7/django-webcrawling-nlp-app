from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
import json
from .models import Games


# Create your views here.

def api(request):
	if request.method == "POST":
		print("POST")
		request_data = request.POST
		name = request_data['yourJavaScriptArrayKey[name]']
		id = request_data['yourJavaScriptArrayKey[id]']
		rating = request_data['yourJavaScriptArrayKey[rating]']
		# img = request_data['yourJavaScriptArrayKey[image]']
		imgback = request_data['yourJavaScriptArrayKey[background_image]']
		metacritic = request_data['yourJavaScriptArrayKey[metacritic]']
		if metacritic == '':
			metacritic = -999
		# request_data = json.loads(request_data)

		new_entry = Games.objects.get_or_create(name = name, id=id, rating=rating,
			imgback=imgback, metacritic=metacritic)[0]

	return render(request, 'api/index.html')
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import Links, Comments
from .comcrawl import CommentsCrawler
import time

# Create your views here.
@csrf_exempt
def crawler(request):
	if request.method == "POST":
		request_data = request.POST
		id = request_data['yourJavaScriptArrayKey[id]']
		link = request_data['yourJavaScriptArrayKey[reddit_url]']
		name = request_data['yourJavaScriptArrayKey[name]']

		new_entry = Links.objects.get_or_create(id = id,
			link=link, name=name)[0]
		crawl = CommentsCrawler()


		if request.GET.get('runningNLP') != None:
			print("button clicked")
			start = time.time()
			crawl.events(link)
			print("Time elapsed:")
			end = time.time()
			print(end - start)
			extracted_commments = crawl.get_comments()

			for i in extracted_commments:
				print(i)
				new_entry2 = Comments.objects.get_or_create(name=name, comment = i)[0]



		# print("button clicked")
		# start = time.time()
		# crawl.events(link)
		# print("Time elapsed:")
		# end = time.time()
		# print(end - start)

		

	return render(request, 'crawler/search.html')
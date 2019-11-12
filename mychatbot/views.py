from django.shortcuts import render
import os
from django.http import HttpResponse, request
from slackclient import SlackClient

# Create your views here.
def first_function(request, template_name = "first.html"):
	
	SLACK_TOKEN = os.environ.get('SLACK_TOKEN', None)
	print(SLACK_TOKEN)
	slack_client = SlackClient(SLACK_TOKEN)
	print(slack_client)

	channels_call = slack_client.api_call("channels.list")
	print(channels_call)
	if channels_call.get('ok'):print(channels_call['channels'])

	SLACK_WEBHOOK_SECRET = os.environ.get('SLACK_WEBHOOK_SECRET',None)
	print(SLACK_WEBHOOK_SECRET)

	if request.method=='GET':
		gg = request.GET.copy()
		dd = gg.get('token')
		channel = gg.get('channel_name')
		print(channel)
		username = gg.get('user_name')
		text = gg.get('text')
		print(text)
		print(username)
		print(channel)
		print
		# inbound_message = username + " in " + channel + " says: " + text
		# print(inbound_message)

	def test():
		return Response('It works!')	

	return render(request, template_name)


def slack(request):
	print("started")
	print(request.method)
	return HttpResponse("running")	
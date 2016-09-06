from django.shortcuts import render
import json, requests, random, re
from pprint import pprint

from django.views import generic
from django.http.response import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from models import *
from wit import Wit
import random
import time
PAGE_ACCESS_TOKEN = "<YOUR PAGE ACCESS TOKEN>"
VERIFY_TOKEN = "<YOUR PAGE VERIFY TOKEN>"
i = 0
general = ["hmmm","hmmm...","ok","oh","ok","ahh","uhh"]
def send(request, response):
    print('Sending to user...', response['text'])

def recieve(request):
    print('Received from user...', request['text'])

actions = {
    'send': send,
    'my_action': recieve,
}

client = Wit(access_token='CVY5ZY46M2GNIJRFN25MHJQNHRETLCTH', actions=actions)
import urllib, requests


# the following need to be in settings.py
LUIS_QUERY_URL = "<LUIS URL>"
APP_ID = "<YOUR LUIS APP ID>"
SUBSCRIPTION_KEY = "<LUIS SUBSCRIPTION KEY>"


def query_luis(message):
    """
    send a message to LUIS
    """
    
    query = {'id':APP_ID,
             'subscription-key':SUBSCRIPTION_KEY,
             'q': urllib.quote_plus(message)}
    message_url = LUIS_QUERY_URL + urllib.urlencode(query)
    r = requests.get(message_url)
    response = r.json()
    if expected_intent:
        info = {}
        for intent in response['intents']:
            if intent['intent'] == expected_intent:
                return response['entities']
            
    return False

def getResponse(question):
    print query_luis(question)
    """
    try:
        if question in general:
            return ""
	question = Question.objects.get(question__icontains=question)	
	objs = question.answer.all()
        if len(objs) > 0:
            return random.choice(objs).answer
        else:
            return "You are not the first one to ask this question.\nI'll update my knowlege base soon "
    except Exception,e:
        print e
        return "Sorry I don't have answer for that.\nI'll update my knowlege base soon"
    """
while True:
    msg = raw_input()
    getResponse(msg)
    
def post_facebook_message(fbid, recevied_message):
    
    response_messages = getResponse(recevied_message)
    #response_messages = getResponse(recevied_message)
    user_details_url = "https://graph.facebook.com/v2.6/%s"%fbid 
    user_details_params = {'fields':'first_name,last_name,profile_pic', 'access_token':PAGE_ACCESS_TOKEN} 
    user_details = requests.get(user_details_url, user_details_params).json()    
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
    response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":response_messages.replace("<br/>","")}})
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)

# Create your views here.
class SmartCQView(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == VERIFY_TOKEN:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')
        
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    # Post function to handle Facebook messages
    def post(self, request, *args, **kwargs):
        # Converts the text payload into a python dictionary
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                if 'message' in message: 
                    post_facebook_message(message['sender']['id'], message['message']['text'])
                           
        return HttpResponse()  

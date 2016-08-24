import requests,urllib

LUIS_QUERY_URL = "https://api.projectoxford.ai/luis/v1/application?"
APP_ID = "d7681133-d480-4c00-9fb2-ff9e73fd096a"
SUBSCRIPTION_KEY = "c08f2b88f18841599cbcaf24c639dc49"


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
    info = {}
    return response['intents']


def getResponse(question):
    print query_luis(question)

while True:
    msg = raw_input()
    getResponse(msg)

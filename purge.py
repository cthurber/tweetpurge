import tweepy

 # Returns information from Twitter API information file
def getKey(apiFile):
    apiInfo = []
    with open(apiFile,'r') as info:
        for line in info:
            apiInfo.append(line.strip('\n'))
    info.close()
    return apiInfo # [0:consumer_key,1:consumer_secret,2:access_token,3:access_token_secret]

# Authentication details
apiKey = getKey('.apikey') # Returns [0:consumer_key,1:consumer_secret,2:access_token,3:access_token_secret]
consumer_key = apiKey[0]
consumer_secret = apiKey[1]
access_token = apiKey[2]
access_token_secret = apiKey[3]

# Create authentication token
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Get all tweets for the account
# API is limited to 350 requests/hour per token
# so for testing purposes we do 10 at a time
api = tweepy.API(auth)
timeline = api.user_timeline(count = 10)

api.destroy_status(t.id)

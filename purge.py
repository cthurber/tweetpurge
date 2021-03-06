import tweepy,os,sys

# Checks to see if environment is properly setup, runs setup if not
def checkEnv():
    if os.path.isfile('tweets.csv') == False:
        print("Could not find 'tweets.csv'")
        print("Please download a Twitter archive and place the CSV in this directory before trying again")
        sys.exit(0)

# Returns information from Twitter API information file
def writeCredentials():
    print("\n === Tweet Purge Setup === ")
    password = input("Enter your twitter username: ")
    details = [encrypt(password,input("API Key: ")),encrypt(password,input("API Secret: ")),encrypt(password,input("Token: ")),encrypt(password,input("Token Secret: "))]
    # key = encrypt(input("API Key: "))
    # secret = encrypt(input("API Secret: "))
    # token = encrypt(input("Token: "))
    # token_secret = encrypt(input("Token Secret: "))
    with open('.apikey','wb') as apidetails:
        for detail in details:
            apidetails.write(detail)
    getCredentials()

def getCredentials():
    if os.path.isfile('.apikey'):
        password = input("Enter your twitter username: ")
        apiArray = []
        with open('.apikey','rb') as apidetails:
            for line in apidetails:
                apiArray.append(decrypt(password,apidetails.readline().decode('utf8')))
        apidetails.close()
        return apiArray # [0:consumer_key,1:consumer_secret,2:access_token,3:access_token_secret]
    else:
        writeCredentials()

def getIgnores():
    ignoreArray = []
    with open('.ignoreIDs','r') as ignoreFile:
        for line in ignoreFile:
            ignoreArray.append(line.strip('\n'))
    ignoreFile.close()
    return ignoreArray

# Returns a twitter api module made from info file
def makeAPI():
    # Authentication details
    apiInfoArray = getCredentials()
    consumer_key = apiInfoArray[0]
    consumer_secret = apiInfoArray[1]
    access_token = apiInfoArray[2]
    access_token_secret = apiInfoArray[3]
    # Create authentication token
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Get all tweets for the account
    # API is limited to 350 requests/hour per token
    # so for testing purposes we do 10 at a time
    apim = tweepy.API(auth)
    return apim

# TODO Add ability to get within timeframe
def search(dumpCSV):
    dumpArray = []
    searchTerms = []
    done = False
    print("\n === Tweet Purge === ")
    print(" (Enter 'null' to terminate) ")

    while done == False:
        term = input("Look for: ")
        if term != "null":
            searchTerms.append(term)
        else:
            done = True
    if os.path.isfile('deleted_tweets.csv') == False:
        with open("deleted_tweets.csv",'w') as out:
            print("ID,Date,Text",file=out)
        out.close()
    output = open("deleted_tweets.csv",'a')
    with open(dumpCSV,'r') as userTimeline:
        for line in userTimeline:
            info = line.strip('\n').split(",")
            if len(info) > 5:
                for term in searchTerms:
                    text = info[5]
                    if term in text:
                        tweetDate = info[3].split(" ")[0].strip('"')
                        ID = info[0].strip('"')
                        print(ID+","+tweetDate+","+text,file=output)
                        dataArray = [ID,tweetDate,text]
                        dumpArray.append(dataArray)
    output.close()
    return dumpArray

def destroy(tweetid):
    api = makeAPI()
    api.destroy_status(tweetid)

def purge(dumpFile):
    count = 0
    tweetsToPurge = search(dumpFile)
    ignoreIDs = getIgnores()
    ignoreStore = open('.ignoreIDs','a')
    for tweet in tweetsToPurge[:-1]:
        if count < 10:
            if tweet[0] not in ignoreIDs:
                print("\nDate:",tweet[1])
                print("Tweet:",tweet[2])
                delete = input("Delete this tweet? (y/n): ")
                if delete == 'y':
                    print(tweet[0],file=ignoreStore)
                    destroy(tweet[0])
                    count+=0
                elif delete == 'n': # Add to ignore file only
                    print(tweet[0],file=ignoreStore)
                    print("Did not delete above tweet.")
                else:
                    print("Did not delete above tweet.")
        else:
            print("API limit reached. Try again in 15 minutes.")
            break

# checkEnv()
purge('tweets.csv')

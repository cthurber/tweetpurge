# TweetPurge

#### Coming soon: TweetDelete Web App
- [ ] Log in and view your timeline in reverse chron. order
- [ ] Check off all of those tweets from a younger you
- [ ] Hit the big red DELETE button, and enjoy a clean feed!

### Getting Started
#### What you need:
- A Twitter account
- The 'tweets.csv' file from your twitter profile
  - You can [request this file from the Settings page on your Twitter profile](https://support.twitter.com/articles/20170160). 
    Once you download the folder, simply copy the 'tweets.csv' file into the same 
    directory as this python program to get started
- Python 3.x and [Tweepy Twitter API library](http://www.tweepy.org)

#### Example Search:
```
python3.4 ./purge.py
 === Tweet Purge ===
 (Enter 'null' to terminate)
Look for: cookies
Look for: null

Date: 2015-03-22
Tweet: "RT @Josh: Is there a way to replace the OS X beachball with the girl scout cookie finder spinner thingy? http://t.co/5OMidCIZED"
Delete this tweet? (y/n): 
```
Above is an example of the command prompt. ```Purge.py``` 
will prompt you first for terms that you want to search for in your ```tweets.csv``` file.
You can enter as many terms as you like, separating each with the Enter key. 
To finish entering search terms, type ```null``` and hit Enter again.
You will then be prompted with each tweet, and an option to delete it. Hitting any key besides ```'y'``` will not delete the tweet. 
The program will terminate when the API limit has been reached. (A 404 error will appear in the console; a throttled version is in the works)

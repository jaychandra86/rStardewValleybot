# rStardewValleybot
This script will take posts from r/stardewvalley on reddit and post them on twitter.

#Requirements
*Python 3.6 or above
*tweepy - type 'pip install tweepy' in terminal
*praw - type 'pip install praw' in terminal
*requests - type 'pip install requests' in terminal

#Usage
Clone the repository then edit the config.py file with your API keys and Token keys

config.py looks something like this

*Twitter consumer keys and access tokens, used for OAuth
*You can get all of these keys from https://developer.twitter.com

consumer_key = 'put you twitter api key here'
consumer_secret = 'twitter api secret key'
access_token = 'access token here'
access_token_secret = 'access token secret here'

*Reddit client ID and client secret keys here
*You can get your client ID and client secret from https://reddit.com/prefs/apps

username = "your reddit username"
password = "your reddit password"
client_id = "client id"
client_secret = "client secret"

*Once you are done with the config.py
Edit the run.py file for your needs.
You need to edit the subreddit name and line 69 then edit the title in line 75.
That's all you need to do.

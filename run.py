import tweepy
import config
import praw
import prawcore
import time
import requests

#Login to Reddit
def loginToReddit():
    try:
        print("-----------------------------------------------")
        print('* Logging into Reddit Account')
        reddit = praw.Reddit(client_id=config.client_id,
                             client_secret=config.client_secret,
                             password=config.password,
                             user_agent='Stardew Valley bot for twitter by u/_jaypatel'
                             , username=config.username)
        print('* Login successful')
        print('-----------------------------------------------')
        return reddit
    except:
        print('* Login failed')
        print('-----------------------------------------------')

#Grabs an image from Reddit
def grabNewImage(url):
    print("-----------------------------------------------")
    print('* Fetching wallpaper from the Reddit')
    try:
        r = requests.get(url)
        with open('img.jpg', 'wb') as image:
            image.write(r.content)
            image.close()
        print('* Image saved successfully')
    except:
        print('* Something went wrong while downloading image')
        print("-----------------------------------------------")

#Posts the image to twitter
def postTweet(title):
    try:
        print("-----------------------------------------------")
        print('* Logging into twitter')
        auth = tweepy.OAuthHandler(config.consumer_key,
                                   config.consumer_secret)
        auth.set_access_token(config.access_token,
                              config.access_token_secret)

        api = tweepy.API(auth)
        print('* Login successful')

        tweet = title
        image_path = 'img.jpg'

        print('* Posting on twitter')
        #status = api.update_with_media(image_path, tweet)
        api.update_with_media(image_path, tweet)
        #api.update_status(status=tweet)
        print("* Successfully posted")
        print("-----------------------------------------------")
    except:
        print('* Something went wrong while posting tweet')
        print("-----------------------------------------------")


def main():
    reddit = loginToReddit()
    try:
        for submission in reddit.subreddit("stardewvalley").hot(limit=5):
            #you can scrape any subreddit posts, just replace "stardewvalley" with the subreddit you want to scrape, like "memes" or "dankmemes"
            #limit in the above line will give 5 posts from Redditi, change it to whatever you like.
            print("-----------------------------------------------")
            print("* Fetching submission from reddit")
            title = submission.title #title is the title of reddit post
            title = title + ". posted by u/" + str(submission.author) + " #StardewValley #Stardew"
            #above line concatenates title with username of the user whose post is being downloaded and hash tags stardewvalley and stardewy
            #you may need to edit title for your needs
            url = submission.url
            if 'jpg' in url:
                grabNewImage(url)
                postTweet(title)
                time.sleep(20)
            elif 'png' in url:
                grabNewImage(url)
                postTweet(title)
                time.sleep(20)
            else:
                print("* Not an image url")

            print("-----------------------------------------------")
    #exception handling
    except prawcore.exceptions.ServerError as e:
        print(e)
        time.sleep(20)
        pass

    #excepts errors like rate limit
    except praw.exceptions.APIException as e:
        print(e)
        time.sleep(60)

    #excepts other PRAW errors
    except praw.exceptions.PRAWException as e:
        print(e)
        time.sleep(20)

    #excepts network connection errors
    except prawcore.exceptions.RequestException:
        print("* Please check your network connection")
        print("* Sleeping for 1 minute")
        print("---------------------------------------")
        time.sleep(60)


#running the main function
if __name__ == "__main__":
    main()

#Uncomment the following code if you want to run this script forever.
"""
while True:
    if __name__ == "__main__":
        main()
"""

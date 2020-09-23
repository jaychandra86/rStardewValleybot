import tweepy
import config
import praw
import prawcore
import time
import requests


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
        for submission in reddit.subreddit("stardewvalley").hot(limit=8):
            #change stardewvalley to whatever subreddit you want, like memes, dankmemes
            if submission.stickied == False:
                print("-----------------------------------------------")
                print("* Fetching submission from reddit")
                postUrl = "redd.it/" + str(submission)
                #you might need to edit the title too
                title = submission.title
                title = title + ". posted by u/" + str(submission.author) + ". Post url: " + postUrl + " #StardewValley #Stardew"
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



if __name__ == "__main__":
    main()

import tweepy, time, os, random
from datetime import datetime
import config, algorithm

client = tweepy.Client(config.token, config.api_key, config.api_secret, config.access_token, config.access_token_secret)

def retweet(tweetid : int):
    try:
        api = tweepy.API(auth)
        api.retweet(tweetid)
        return True
    except Exception as error:
        print(f"Um erro ocorreu ao tentar retweetar o tweet de ID {tweetid}!\n{str(error)}")
        return False

class MyStream(tweepy.StreamingClient):

    def on_connect(self):
        print(
            f"--------------------\nBot iniciado com sucesso!\n--------------------"
        )

    def on_tweet(self, tweet):
        try:
            if algorithm.check(tweet.text) and tweet.referenced_tweets is None and retweet(tweet.id):
                print(f'{datetime.now()} | Tweet de ID {tweet.id} retweetado com sucesso!')
                print(int(datetime.now().hour))
                if int(datetime.now().hour) > 7 and not int(datetime.now().hour) < 21:
                    time.sleep(random.randint(20, 50))
                time.sleep(10, 30)
        except Exception as error:
            print('--------------------' + str(error) + '--------------------')

    def on_connection_error(self):
        print("Um erro na conexão foi encontrado, o cliente esperará 1 minuto até voltar a funcionar...")
        time.sleep(60)


stream = MyStream(bearer_token=config.token)
add_rules = False # set it to "True" if you need to add the rules

if add_rules:
    try:
        for word in config.words:
            stream.add_rules(
                tweepy.StreamRule(word)
            )
    except Exception as erro:
        print(f"Um erro ocorreu!\n'{str(erro)}'\nO bot irá continuar a funcionar mesmo assim.")

os.system('clear && rm -rf __pycache__ && echo "Iniciando bot..."')

auth = tweepy.OAuthHandler(config.api_key, config.api_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

stream.filter(tweet_fields=["referenced_tweets"])

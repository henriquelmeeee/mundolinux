import tweepy, time, os, random
from datetime import datetime
import config

client = tweepy.Client(config.token, config.api_key, config.api_secret, config.access_token, config.access_token_secret)

def check_words(text : str):
    word = ''
    for letter in text:
        word = word.lower()
        if letter == ' ':
            if word in config.words_not_accepted:
                return False
            word = ''
        if letter in config.words_not_accepted:
            return False
        word = word.replace(' ', '') + letter
    return True if not word in config.words_not_accepted else False

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
        if check_words(tweet.text) and tweet.referenced_tweets is None and retweet(tweet.id):
            print(f'{datetime.now()} | Tweet de ID {tweet.id} retweetado com sucesso!')
            time.sleep(random.randint(150, 250))

    def on_connection_error(self):
        print("Um erro na conexão foi encontrado, o cliente esperará 1 minuto até voltar a funcionar...")
        time.sleep(60)


stream = MyStream(bearer_token=config.token)

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

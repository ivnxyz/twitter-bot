import tweepy

class TweepyWrapper:

  def __init__(self, consumer_key, consumer_secret, access_key, access_secret):
    # Configurar tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)

    # Almacenar referencia a la API
    self.api = tweepy.API(auth)
  
  def get_weet_by_id(self, tweet_id):
    # Obtiene un tweet por su id
    return self.api.get_status(tweet_id)

  def reply_to_tweet(self, username, tweet_id, text):
    # Generar texto del tweet
    final_text = '@{} "{}"'.format(username, text)
    self.api.update_status(final_text, in_reply_to_status_id=tweet_id)
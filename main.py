# Importar dependencias
import tweepy
from tweepy_wrapper import TweepyWrapper
from mentions_listener import MentionsListener
from credentials import CREDENTIALS

# Crear instancia de TweepyWrapper
tweepy_wrapper = TweepyWrapper(CREDENTIALS['CONSUMER_KEY'], CREDENTIALS['CONSUMER_SECRET'], CREDENTIALS['ACCESS_KEY'], CREDENTIALS['ACCESS_SECRET'])

# Escuchar las menciones
mentions_listener = MentionsListener(tweepy_wrapper)

stream = tweepy.Stream(tweepy_wrapper.api.auth, mentions_listener)
stream.filter(track=['@MemefyBot'])
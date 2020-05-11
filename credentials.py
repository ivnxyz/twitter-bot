import os
from dotenv import load_dotenv

load_dotenv()

CREDENTIALS = {
  'CUSTOMER_KEY': os.environ['CONSUMER_KEY'],
  'CONSUMER_SECRET': os.environ['CONSUMER_SECRET'],
  'ACCESS_KEY': os.environ['ACCESS_KEY'],
  'ACCESS_SECRET': os.environ['ACCESS_SECRET']
}
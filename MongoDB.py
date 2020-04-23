import os

MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
#MONGO_HOST = os.getenv("MONGO_HOST","localhost")

print(MONGO_HOST)
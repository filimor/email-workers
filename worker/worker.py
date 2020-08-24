import redis
import json
from time import sleep
from random import randint

if __name__ == '__main__':
  r = redis.Redis(host='queue', port=6379, db=0)
  print('Waiting for messages...')
  while True:
    message = json.loads(r.blpop('sender')[1])
    # Simulating e-mail sending...
    print('Enviando a mensagem:', message['subject'])
    sleep(randint(15,45))
    print('Mensagem', message['subject'], 'enviada')
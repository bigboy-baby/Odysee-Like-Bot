#Code by bigboybigboi#0001 skid if ur homosexual (ew)
import requests, threading, json

with open('config.json') as config_file:
  config = json.load(config_file)

def like(claim,prox):
  proxy = {
    "http":f"http://{prox}",
    "https":f"http://{prox}",
  }
  while True:
    try:
      r = requests.get('https://api.odysee.com/user/new', proxies=proxy)
      dat = r.json()
      token1 = dat['data']
      token = token1['auth_token']

      d = {
        'auth_token': token,
        'claim_ids': claim,
        'type': 'like',
        'clear_types': 'dislike'
      }

      r = requests.post('https://api.odysee.com/reaction/react', data=d, proxies=proxy)
    
      print(f"{token} | Liked {claim}")    
    except:
      pass

claim = input("Claim ID: ")
am = int(input("Thread Amount: "))

prox = config["proxy"]
for n in range(am):
  x = threading.Thread(target=like, args=(claim,prox))
  x.start()

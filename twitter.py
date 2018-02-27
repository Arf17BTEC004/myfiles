import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "jifh8dyfkjchuywhdiqeyuy7etkefu7",
    "consumer_secret"     : "jfuygiuh89 vx98eri788eiefuyh78",
    "access_token"        : "huify8idhfgsuisgtxufkfhyxt78ydhvdghw",
    "access_token_secret" : "huisdcihfwdxdtwuyhjbghfdwhdhtuwsbgsf" 
    }

  api = get_api(cfg)
  tweet = "heyy!"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
print(success)

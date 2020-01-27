import tweepy    #Twitter API-Handling Module
import markovify #Makrov-chain Module
import itertools

def paginate(iterable, page_size):
    while True:
        i1, i2 = itertools.tee(iterable)
        iterable, page = (itertools.islice(i1, page_size, None),
                list(itertools.islice(i2, page_size)))
        if len(page) == 0:
            break
        yield page
        
#This function pulls 20,000 of a user's tweets and downloads them to a .txt file:
def get_tweets(username):
    consumer_key = "IdXm0FUAoMQIz9ODmAR5tz5We"
    consumer_secret = "sUynF60itvxHgMwlRlesyCBDArvUzkDHAtl2L5g2HpqY6uAWFO" 
    access_key = "1054844277480738816-0DzeNjpzHrGR10F2er8NHBNGY51kjX"
    access_secret = "1LldHOnJyw1HX1UOMoilShpo4d1LuFiEHIk97DdEcT5pf"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    auth.set_access_token(access_key, access_secret)

    api = tweepy.API(auth)
    
    tweets = api.user_timeline(screen_name=username)

    for page in paginate(tweets, 100):
        results = [tweet.text for tweet in tweets]
        for result in results:
            print(result)
    #print(tweets)
    tmp=[]
    # "dict" removes emojis and extranneous characters that can't be compiled into file 
    dict = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYS \n.-,?!#$%&+_@'():;1234567890"
    
    tweets_for_csv = [tweet.text for tweet in tweets]
    for x in tweets_for_csv:
        tmp.append("\n\n")
        #tmp.append(username)
        #tmp.append(" said: ")
        
        for y in x:
            if y in dict:
                tmp.append(y)
                
          
    tmp = "".join(tmp)                
    #print(tmp)
    download_dir = input("Enter The Name of File To Save (.txt): ")
    txtfile = open(download_dir, "w")
    txtfile.write("".join(tmp))
    return(download_dir) #<-- markov_tweets only needs to take in the filename

#This function generates 200 Markov-Chain tweets that are unique in respect to eachother:

def markov_tweets(file):
    with open(file) as f:
        text = f.read()

    text_model = markovify.Text(text)

    list = []
    while ((len(list)) < 200):
        x = (text_model.make_short_sentence(140)) #Generate Markov-Chain  140 characters long
        if x not in list:
            list.append(x)
            print("\n", x)
    


if __name__ == '__main__':
    
    user = input("Enter a Twitter Username: @")
    
    infile = get_tweets(user)

    markov_tweets(infile)

    
   
    
    

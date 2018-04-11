from TwitterSearch import *
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
import string

def tweetSearch( handle, opt ):
    try:
        tuo = TwitterUserOrder( handle )
        db = {}
        hashes = {}

        ts = TwitterSearch(
                consumer_key = 'ab2nEDDA5f45BX5pve12mtOZZ',
                consumer_secret = 'EuHOzITfqFZlByiaX8gsl4atP0pWZSoVAXzQc5nMK85IpJtabx',
                access_token = '2859709127-aFs9NZr4KByeaZzdPm8lULHdltQ7Ak4XU1oS79d',
                access_token_secret = 'HfBsv4mwbTAb1oNa9jPk5lUMRgwLqdzBm1mkutQrmMY0j'
            )

        for tweet in ts.search_tweets_iterable(tuo):
            analyze(db, tweet['text'], hashes, opt);

    except TwitterSearch as e:
        print(e)
    if(opt == 0):
        return db;
    else:
        return hashes;

def analyze( db, text, hashes, opt ):
    textArr = text.split()

    #if user asking for list of 10 most common words
    if(opt == 0):
        stops = set(stopwords.words('english'))
        punctuations = set(string.punctuation)
        for text in textArr:
            text = text.encode('utf-8')
            if(text.lower() not in stops and text.lower() not in punctuations and text[0] not in punctuations):
                if(text not in db):
                    db[text] = 1;
                else:
                    db[text] += 1;
    #if user asking for list of 10 most common hashtags
    elif(opt == 1):
        for text in textArr:
            text = text.encode('utf-8')
            if(text[0] == '#'):
                if(text not in hashes):
                    hashes[text] = 1;
                else:
                    hashes[text] += 1;
    return;

#prints out the 10 most common values as designated by the user
def list_values(handle, opt):
    db = tweetSearch(handle, opt)
    #since db is not sorted, need to sort by value
    sorted_db = sorted(db, key=lambda x: db[x], reverse=True)

    count = 0
    for k in sorted_db:
        if(count < 10):
            print "{}       {}".format(k, db[k])
            count += 1
        else:
            break

list_values("mcuban", 0)
list_values("mcuban", 1)

from spacy.en import English
from textblob import TextBlob
from twitter_helper import Twitter_helper
from csv_helper import Csv_helper
import re

tweets = Twitter_helper.search_tweets("#BOE",10000)
for tweet in tweets:
    tweet.text = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)","",tweet.text).replace("RT","")
    sentiment = TextBlob(tweet.text).sentiment
    tweet.polarity=sentiment[0]
    tweet.subjectivity=sentiment[1]
Csv_helper.write_to_file(tweets,"tweets")


'''
nlp = English()

doc = nlp("Make no mistake our current economic troubles are the direct result of this Tory gov't cynical political manoeuvrings")
print(doc)

for token in doc:
    print (token)
    #print(token.lemma_)
    #print(token.pos_)
for sent in doc.sents:
    print(sent)
for ent in doc.ents:
    print(ent)
    print("type:"+ent.label_)
for np in doc.noun_chunks:
    print(np)


for sent in doc.sents:
    print(sent)
    print(TextBlob(str(sent)).sentiment)
'''
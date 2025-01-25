from textblob import TextBlob

with open('my_text.txt', 'r') as f:
    text=f.read()

blob= TextBlob(text)
# will give the value between -1 to 1;
sentiment = blob.sentiment.polarity 
print(sentiment)


 
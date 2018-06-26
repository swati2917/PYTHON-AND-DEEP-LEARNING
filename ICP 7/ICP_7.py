import urllib.request
from bs4 import BeautifulSoup
import nltk
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.util import ngrams


f= open("input.txt","w+", encoding="utf-8")

# Assigning link to a variable
myLink = "https://en.wikipedia.org/wiki/Python_(programming_language)"

# Opens the URL
getLink=urllib.request.urlopen(myLink)

# Converts to HTML
soup = BeautifulSoup(getLink,  "html.parser")
text = soup.get_text()
f.write(soup.get_text())

# Tokenization the text in the URL given
stokens = nltk.sent_tokenize(text)
wtokens = nltk.word_tokenize(text)

# Printing Tokenized Sentences
for s in stokens:
    print(s)
# Printing Tokenized Words
for w in wtokens:
    print(w)

# Stemming the text in the URL given
ps = PorterStemmer()
ls = LancasterStemmer()
ss = SnowballStemmer('english')
print("Stemming Output")
for words in wtokens:
    print("Porter stemming Output")
    #print(ps.stem(words))
    print("Lancaster stemming Output")
    #print(ls.stem(words))
    print("Snowball stemming Output")
    #print(ss.stem(words))


# Lemmatization
lemmatizer = WordNetLemmatizer()
print("Lemmatized Output")
#print(lemmatizer.lemmatize(text))

# Parts of speech
for w in wtokens:
    print("POS output")
   # print(nltk.pos_tag(w))

# Named Entity Recognition
sentence = "The grapevine has it that disgruntled Congressmen are looking to join hands with BJP to bring down Karnataka government"
print(ne_chunk(pos_tag(word_tokenize(sentence))))

# Trigram
mySentence = "Hi How are you? i am fine and you"
token=nltk.word_tokenize(mySentence)
trigram = ngrams(token,3)
for t in trigram:
    print(t)
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

#This list will contain the character names
names = []
#This will contain the dialogue by a particular character
text = []

Captain_America = []
Iron_Man = []
Thor = []
Hulk = []
Black_Widow = []
Black_Panther = []
Winter_Soldier = []
Hawkeye = []
Vision = []
Nick_Fury = []
Scarlett_Witch = []

#List of urls to fetch the transcripts from
url = ["https://transcripts.fandom.com/wiki/The_Avengers","https://transcripts.fandom.com/wiki/Avengers:_Age_of_Ultron","https://transcripts.fandom.com/wiki/Avengers:_Infinity_War","https://transcripts.fandom.com/wiki/Avengers:_Endgame"]
for site in url:
    html_content = requests.get(site).text
    soup = BeautifulSoup(html_content , "lxml")

    for x in soup.find_all('p'):
        dialogue = x.get_text()
        before_colon = re.findall ("(.*?):", dialogue)
        if len(before_colon) == 0:
            pass
        else:
            names.append(before_colon[0].lower().strip())
            after_colon = re.findall (":(.*)", dialogue)
            text.append(after_colon[0].lower().strip())
            before_colon.clear()
            after_colon.clear()

data = {'Character_Names': names}
df = pd.DataFrame(data)

#Checked the unique characters from the names list here to help me with the if conditon
un = pd.unique(df['Character_Names'])

for x in range(len(names)):
    if names[x] == "nick fury" or names[x] =="fury" or names[x] =="nick fury (v.o.)" or names[x] =="nick fury (o.s.)":
        Nick_Fury.append(text[x])
        
    elif names[x] == "natasha romanoff" or names[x] =="black widow (v.o.)" or names[x] =="black widow" or names[x] =="natasha" or names[x] =="natasha romanonff" or names[x] =="natasha romanoff (2012)" or names[x] =="natasha (memory)":
        Black_Widow.append(text[x])
        
    elif names[x] == "bruce" or names[x] =="banner" or names[x] =="banner (coming to)" or names[x] =="hulk" or names[x] =="bruce banner" or names[x] =="bruce banner *out of breath*" or names[x] =="hulk (2012)" or names[x] =="bruce banner (2023)" or names[x] =="bruce (memory)":
        Hulk.append(text[x])

    elif names[x] == "steve" or names[x] =="captain america" or names[x] =="captain america (v.o.)" or names[x] =="steve (v.o.)" or names[x] =="steve rogers" or names[x] =="steve rogers (2012)" or names[x] =="captain stevens (steve rogers)":
        Captain_America.append(text[x])

    elif names[x] == "tony" or names[x] =="iron man" or names[x] =="tony (cont'd) (to thor)" or names[x] =="tony (v.o.)" or names[x] =="iron man (v.o.)" or names[x] =="tony stark" or names[x] =="tony stark *under his breath*" or names[x] =="tony stark (2012)" or names[x] =="tony stark(2012)" or names[x] =="tony stark (2023)" or names[x] =="tony stark (voiceover)" or names[x] =="tony stark (hologram)":
        Iron_Man.append(text[x])

    elif names[x] == "thor" or names[x] =="thor (2012)":
        Thor.append(text[x])

    elif names[x] == "hawkeye" or names[x] =="clint" or names[x] =="barton" or names[x] =="clint barton" or names[x] =="hawkeye (v.o.)" or names[x] =="clint barton (2012)" or names[x] =="clint barton (2023)":
        Hawkeye.append(text[x])

    elif names[x] == "wanda maximoff":
        Scarlett_Witch.append(text[x])

    elif names[x] == "vision":
        Vision.append(text[x])

    elif names[x] == "t'challa" or names[x] =="king t'challa":
        Black_Panther.append(text[x])

    elif names[x] == "bucky barnes":
        Winter_Soldier.append(text[x])

#Enter the character name for which you want the wordcloud to be displayed. I have used Captain America as sn example.
text_CA = " ".join(review for review in Captain_America)
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text_CA)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

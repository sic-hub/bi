import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
quotes = []
authors = []

for quote in soup.find_all('span', class_='text'):
    quotes.append(quote.get_text())
for author in soup.find_all('small', class_='author'):
    authors.append(author.get_text())

data_df = pd.DataFrame({'Quote': quotes, 'Author': authors})
author_counts = data_df['Author'].value_counts()

plt.figure(figsize=(13,8))
sns.barplot(x=author_counts.index, y=author_counts.values)
plt.title('Number of Quotes by Author')
plt.xlabel('Author')
plt.ylabel('number of quotes')
plt.xticks(rotation=15)
plt.show()

data_df.to_csv(r'P4 scraped quotes.csv')
print("saved")





"""
,Quote,Author
0,“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”,Albert Einstein
1,"“It is our choices, Harry, that show what we truly are, far more than our abilities.”",J.K. Rowling
2,“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”,Albert Einstein
3,"“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”",Jane Austen
4,"“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”",Marilyn Monroe
5,“Try not to become a man of success. Rather become a man of value.”,Albert Einstein
6,“It is better to be hated for what you are than to be loved for what you are not.”,André Gide
7,"“I have not failed. I've just found 10,000 ways that won't work.”",Thomas A. Edison
8,“A woman is like a tea bag; you never know how strong it is until it's in hot water.”,Eleanor Roosevelt
9,"“A day without sunshine is like, you know, night.”",Steve Martin
"""

import nltk
from newspaper import Article

# select a url of any news article
url = 'https://timesofindia.indiatimes.com/india/coronavirus-in-india-live-updates-indias-weekly-covid-toll-has-fallen-by-88-since-september-peak/liveblog/80620726.cms'
article = Article(url)
article.download()
article.parse()
nltk.download('punkt')
article.nlp()

print(article.text)
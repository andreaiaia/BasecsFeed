import feedparser
News = feedparser.parse("https://medium.com/feed/basecs")
first = News.entries[1]

print(first.keys())

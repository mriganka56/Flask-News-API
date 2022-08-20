from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)
newsapi = NewsApiClient(api_key='259f102d55d942a783bd1f91a8eef0d6')


@app.route('/')
@app.route('/home')
def home():
    
    top_headlines = newsapi.get_top_headlines(
                                          category='general',
                                          language='en',
                                          country='in')    
    articles = top_headlines['articles']
    articles_list = extract(articles)
    return render_template('home.html',articles_list=articles_list)


def extract(articles):
    desc,news,img,url = [],[],[],[]
    
    for i in range(len(articles)):
        my_articles = articles[i]
        
        news.append(my_articles['title'])  
        desc.append(my_articles['description'])
        img.append(my_articles['urlToImage'])
        url.append(my_articles['url'])
        
    my_list = zip(desc, news, img, url)
    return my_list

if __name__=="__main__": 
    app.run(debug='False')


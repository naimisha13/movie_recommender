# __author:Smita Nannaware
# data:3/31/2022
from flask import Flask, render_template, request

#import model_recommender
from model_recommender import get_recommendations

app = Flask(__name__)


# default-page
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def getMovies():
    search_text = request.form.get('searchText')
    print(search_text)
    movieList = get_recommendations(search_text).tolist()
    print(movieList)
    return render_template('results.html', movieList=movieList)


if __name__ == '__main__':
    app.run()
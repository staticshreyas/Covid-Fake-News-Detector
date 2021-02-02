#Importing the Libraries
import flask
from flask import Flask, request,render_template
from flask_cors import CORS
import os
import pickle
import newspaper
from newspaper import Article
import urllib
import nltk

#Loading Flask and assigning the model variable
app = Flask(__name__)
CORS(app)
app=flask.Flask(__name__,template_folder='templates')

# Loading the model
with open('model.pickle', 'rb') as handle:
	model = pickle.load(handle)

@app.route('/')
def main():
    return render_template('main.html')

#Receiving the input text from the user
@app.route('/predict',methods=['GET','POST'])
def predict():
    # Data recieved
    url = request.get_data(as_text=True)[5:]
    url = urllib.parse.unquote(url)

    article=Article(str(url),language="en")
    article.download()
    article.parse()
    nltk.download('punkt')
    article.nlp()

    summary=article.summary
    
	# Predicting the input
    pred = model.predict([summary])

    return render_template('main.html', prediction_text='The news is "{}"'.format(pred[0]))
    
if __name__=="__main__":
    port=int(os.environ.get('PORT',5000))
    app.run(port=port,debug=True,use_reloader=False)
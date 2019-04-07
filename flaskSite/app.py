# import the Flask class from the flask module
from flask import Flask, render_template
from support.textFreq import textFreqCal

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return render_template('index.html')  # render a template


@app.route('/termsService')
def termsService():
    topNRankNum = 5

    resText,resRank, mainContract = textFreqCal(topNRankNum)


    return render_template('termsOfService.html', **locals())


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)

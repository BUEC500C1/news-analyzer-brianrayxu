from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/upload/')
def createFile():
    return jsonify({'fileID':'TEST',
                    'size':'TEST'})

@app.route('/textnlp/', methods=['GET', 'POST'])
def sentimentnlp():
    return "Text NLP Stub!"

@app.route('/newsfeed/', methods=['GET', 'POST'])
def createFeed():
    return "Newsfeed Stub!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
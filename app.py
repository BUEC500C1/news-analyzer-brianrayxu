from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/uploader/create')
def createFile():
    return jsonify({'fileID':'TEST',
                    'size':'TEST'})

@app.route('/uploader/delete')
def deleteFile(fileID):
    return jsonify({'fileID':'TEST',
                    'size':'TEST'})

@app.route('/textnlp/', methods=['GET', 'POST'])
def sentimentnlp(inString):
    return "Text Analyzed!"

@app.route('/newsfeed/', methods=['GET', 'POST'])
def createFeed():
    return "Feed Created!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)

from flask import Flask, jsonify
import logging

app = Flask(__name__)

@app.route('/uploader/create')
def createFile():
    logging.info("File Creation Started...")
    logging.info("File Created!")
#    return jsonify({'fileID':'TEST',
#                     'size':'TEST'})
    return "File Created!"


@app.route('/uploader/delete')
def deleteFile(fileID):
    logging.info("File Started...")
    logging.info("File Created!")
#     return jsonify({'fileID':'TEST',
#                     'size':'TEST'})
    return "File Deleted!"


@app.route('/textnlp/', methods=['GET', 'POST'])
def sentimentnlp(inString):
    logging.info("Text Analyzing...")
    logging.info("Text Analyzed!")
    
    return "Text Analyzed!"

@app.route('/newsfeed/', methods=['GET', 'POST'])
def createFeed():
    logging.info("Newsfeed Generating...")
    logging.info("Feed Created!")
    return "Feed Created!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)

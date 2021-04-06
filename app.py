from flask import Flask, jsonify, render_template, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import logging
import pdfreader
from pdfreader import PDFDocument, SimplePDFViewer
import os
import pymongo
from google.cloud import language_v1

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './filestore/'


#mongoDB init
client = pymongo.MongoClient('mongodb+srv://Brian:cyp1b1@cluster0.v056q.mongodb.net/FileDB?retryWrites=true&w=majority')
db = client['FileDB']
collection = db['Files']


@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
    if request.method == 'POST':
        f = request.files['file']
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename))
        f.save(filepath)
        fd = open(filepath, "rb")
        doc = PDFDocument(fd)
        version = doc.header.version
        print(doc.metadata)
        creationDate = doc.metadata.get('CreationDate')
        dataType = doc.metadata.get('Subtype')
        #data methods
        viewer = SimplePDFViewer(fd)
        textData = []
        for canvas in viewer:
            #print(canvas.strings)
            textData += canvas.strings
            tempstring = ''
            textWords = []
            textWhole = ''
            for character in textData:
                if character != ' ':
                    tempstring += character
                else:
                    if tempstring:
                        textWords.append(tempstring)
                        tempstring = ''

        #turn words into whole string for NLP  
        textWhole = ' '.join(textWords)  
        NLPclient = language_v1.LanguageServiceClient.from_service_account_json("./project2-ec601-38fd65cd495b.json")
        document = language_v1.Document(content=textWhole, type_=language_v1.Document.Type.PLAIN_TEXT)
        annotations = NLPclient.analyze_sentiment(request={'document': document})

        score = annotations.document_sentiment.score
        magnitude = annotations.document_sentiment.magnitude


        print(secure_filename(f.filename))
        print(creationDate)
        print(textWords)

        fileDocument = {
            "name" : secure_filename(f.filename),
            "creationDate" : creationDate,
            "text" : textWords,
            "sentiment_score" : score,
            "sentiment_magnitude" : magnitude
        }

        collection.insert_one(fileDocument)
        return (secure_filename(f.filename) + " was uploaded with sentiment_score of " + str(score) + " and magnitude of " + str(magnitude))


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
    app.run(host='0.0.0.0', port=5000)

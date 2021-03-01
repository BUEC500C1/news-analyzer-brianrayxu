from flask import Flask, jsonify
import logging
import pdfreader
from pdfreader import PDFDocument, SimplePDFViewer

#DB Operations
client = pymongo.MongoClient("mongodb+srv://Brian:<password>@cluster0.v056q.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test


app = Flask(__name__)

@app.route('/uploader/create')
def createFile():
    logging.info("File Creation Started...")
    #metadata
    fd = open("Testpdf.pdf", "rb")
    doc = PDFDocument(fd)
    version = doc.header.version
    creationDate = doc.metadata.CreationDate
    dataType = doc.root.Metadata.Subtype
    #data methods
    viewer = SimplePDFViewer(fd)
    for canvas in viewer:
        #make += to contcatenate all textdata
        textData = canvas.strings
    
    
    logging.info("Documenting New File")
    #Add mongo Methods
    
    logging.info("File Created!")
#     return jsonify({'fileName':fileName, 'version': version, 'creationDate': creationDate, 'dataType': dataType, 'text':textData,})
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

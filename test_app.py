from app import *

import pytest

def test_createFile():
  assert createFile() == "File Created!"
   
def test_deleteFile():
  assert deleteFile(12345) == "File Deleted!"
  assert deleteFile("FILENAME") == "fileID needs to be an integer"
    
def test_sentimentNLP():
  assert sentimentNLP(12345) == "Text Analyzed!"
  assert sentimentNLP("abcede") == "fileID needs to be an integer" 

def test_createFeed():
  assert createFeed() == "Feed Created!"
    
 

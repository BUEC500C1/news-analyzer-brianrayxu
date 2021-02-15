# news-analyzer-brianrayxu
News Analyzer API suite using Flask, Google NLP, and ...


## Module Outlines

### I. File Uploader
#### Design
As a user of this API, I would want to be able to:
1. Upload a file successfully into some file storage on the cloud.
2. Have this file be documented in a database for easy access later on.
3. See some confirmation on whether my file was successfully uploaded or not.

This module will be both procedure and entity based. The actual file uploading task will be designed to be procedural based due to the different types of user input. The flexibility offered by a task-by-task API will allow different upload types (jpg, pdf, docx) to have their own individual process flows.

#### Methods
Sample High Level Methods

- createFile(inFile) : Function that completes all necessary tasks upon receiving a new document
  - documentFile : Creates an entry in the database tracking all stored documents. Includes timestamp, size, tags, etc.
  - storeFile(inFile) : Takes in file and stores it in a filestore service (Google Cloud, Azure, etc.)



### II. Text NLP Analysis
#### Design
As a user of this API, I would want to be able to:
1. asdf
2. 1234
3. 1234
#### Methods
Sample High Level Methods

### III. Newfeed Ingestor
#### Design
As a user of this API, I would want to be able to:
1. asdf
2. 1234
3. 1234
#### Methods
Sample High Level Methods

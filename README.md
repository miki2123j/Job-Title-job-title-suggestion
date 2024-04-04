# Job-Title-suggestion

## Description
1. Objective:
- This application aims to analyze the content of a PDF file (typically a CV or resume) and recommend an appropriate job title based on the extracted information.
2. Workflow:
- The application follows these steps:
 1. Read the specified PDF file.
 2. Extract the text content from the PDF.
 3. Uses a pre-trained question-answering model to answer the question: “What is the best job title that would be suitable for this person?”
3. Libraries Used:
- The script utilizes the following Python libraries:
   1. argparse: For handling command-line arguments.
   2. PyPDF2: For reading and extracting text from PDF files.
   3. transformers (from Hugging Face): For loading a pre-trained question-answering model.
   4. pipeline (from Hugging Face): For question-answering tasks.
4. Functionality:
The read_pdf(file_path) function reads the specified PDF file and extracts its text content.
The answer_question(context, question) function uses the question-answering model to suggest a job title based on the provided context (extracted text) and the question.
6. Model Choice:
The application uses the “deepset/roberta-base-squad2” model for question-answering. The reasons behind choosing the “deepset/roberta-base-squad2” model is Contextual Understanding.RoBERTa models capture contextual information effectively. They understand the context in which a question is asked and provide relevant answers. This contextual understanding is crucial for analyzing CVs, as job titles and qualifications depend on the context provided by the candidate’s experience and skills.

## How to install 
</div>
Follow these steps to set up the environment and run the application.

1. Clone this repository to your local machine
2. Create a Python Virtual Environment using the following command:
   - Using [virtualenv](https://learnpython.com/blog/how-to-use-virtualenv-python/):

     _Note_: Check how to install virtualenv on your system here [link](https://learnpython.com/blog/how-to-use-virtualenv-python/).

     ```bash
     virtualenv env
     ```

   **OR**

   - Create a Python Virtual Environment:

     ```bash
     python -m venv env
     ```
3. Activate the virtual environment using the following command:
   - On Windows.

     ```bash
     env\Scripts\activate
     ```

   - On macOS and Linux.

     ```bash
     source env/bin/activate
     ```
4. Install Dependency using the following command:
     ```bash
     pip install -r requirements.txt
     ```
5. Run the application using the following command:
     ```bash
     python app.py data/sampleResume.pdf
     ```
6. If you encounter toch error, try to run the following command:
     ```bash
     pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
     ```

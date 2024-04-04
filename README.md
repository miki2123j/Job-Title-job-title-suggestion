# Job-Title-suggestion

## How to install 
</div>
To run this program, follow the following instructions:

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
5.Run the application using the following command:
     ```bash
     python app.py data/sampleResume.pdf
     ```
6. If you encounter toch error, try to run the following command:
     ```bash
     pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
     ```

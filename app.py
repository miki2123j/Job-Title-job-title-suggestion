import argparse
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
import PyPDF2
import sys


def read_pdf(file_path):
    try:
        with open(file_path, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            num_pages = len(pdf_reader.pages)

            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                page_text = page.extract_text()

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

    return page_text


def answer_question(context, question):
    inputs = {"context": context, "question": question}
    result = qa_pipeline(inputs)
    return result["answer"]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python app.py <path_to_CV>")
    else:
        CV_path = sys.argv[1]
        read_pdf(CV_path)
        context = read_pdf(CV_path)
        question = "what is the best job title that would be suitable for this person?"
        # Load the model and tokenizer
        model_name = "deepset/roberta-base-squad2"
        model = AutoModelForQuestionAnswering.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)
        answer = answer_question(context, question)
        print("The best job title that would be suitable for this person is:", answer)

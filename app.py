import argparse
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
import PyPDF2


def read_pdf(file_path):
    try:
        with open(file_path, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            page_text = ""
            for page in pdf_reader.pages:
                page_text += page.extract_text()
        return page_text
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None


def answer_question(context, question, model_name="deepset/roberta-base-squad2"):
    try:
        model = AutoModelForQuestionAnswering.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)
        result = qa_pipeline({"context": context, "question": question})
        return result["answer"]
    except Exception as e:
        print(f"Error  using the model: {e}")
        return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze CV and suggest job title")
    parser.add_argument("CV_path", help="Path to the CV (PDF file)")
    args = parser.parse_args()

    CV_text = read_pdf(args.CV_path)
    if CV_text:
        question = "What is the best job title that fits the candidate?"
        suggested_title = answer_question(CV_text, question)
        if suggested_title:
            print(
                f"The best job title that would be suitable for this person is: {suggested_title}"
            )


from docx import Document

def replace(filename, old_text, new_text):
    doc = Document(filename)
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            if old_text in run.text:
                run.text = run.text.replace(old_text, new_text)

    doc.save(filename)

test="/mnt/c/Users/joelv/OneDrive/test-python_docs.docx"

replace(test, 'gentile', 'Gentile')

import PyPDF2
import sys

def extract_text(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page in reader.pages:
                text += page.extract_text()
            return text
    except Exception as e:
        return str(e)

cv_text = extract_text('AI-2026-03_CV_Tanushree_L.pdf')
cl_text = extract_text('AI-2026-03_CL_Tanushree_L.pdf')

print("--- CV START ---")
print(cv_text)
print("--- CV END ---")
print("--- CL START ---")
print(cl_text)
print("--- CL END ---")

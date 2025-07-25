import os
from flask import Flask, request, render_template, send_from_directory
import fitz  # PyMuPDF
import openai

app = Flask(__name__, static_folder='static', template_folder='templates')

# Zet hier je eigen OpenAI API-key in
openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def summarize_with_openai(text):
    prompt = (
        "Vat onderstaande tekst samen in duidelijke bulletpoints. "
        "Focus op de hoofdpunten, acties of belangrijke informatie.\n\n"
        f"Tekst:\n{text}\n\nBulletpoints:"
    )
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response.choices[0].message['content'].strip()

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = None
    error = None

    if request.method == 'POST':
        text = request.form.get('text')
        pdf_file = request.files.get('pdf')

        if pdf_file and pdf_file.filename.endswith('.pdf'):
            text = extract_text_from_pdf(pdf_file)
        elif not text:
            error = "Geen tekst of PDF ontvangen."
            return render_template('index.html', summary=None, error=error)

        summary = summarize_with_openai(text)

    return render_template('index.html', summary=summary, error=error)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


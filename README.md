# Email & PDF Samenvattingstool

Deze tool laat gebruikers een e-mail of PDF uploaden en vat de inhoud samen in bulletpoints via de ChatGPT API.

## Installatie lokaal

1. Clone deze repo:
   ```
   git clone https://github.com/jouw-gebruikersnaam/email-pdf-summarizer.git
   cd email-pdf-summarizer
   ```

2. Installeer dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Voeg je OpenAI API-key toe:
   ```
   export OPENAI_API_KEY=sk-...
   ```

4. Start de app:
   ```
   python app.py
   ```

App draait op `http://localhost:5000`.

## Deployment op Render.com

1. Maak een Render-account aan
2. Koppel deze GitHub-repo
3. Voeg `OPENAI_API_KEY` toe als environment variable
4. Build command: `pip install -r requirements.txt`
5. Start command: `python app.py`

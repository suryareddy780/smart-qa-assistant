# Smart Q&A Assistant

A beginner-friendly Python + Streamlit project demonstrating:
- **Role prompting** — define the assistant's role (for example, “You are a helpful tutor”).
- **Few-shot examples** — provide example question/answer pairs to guide response format.
- **Different prompt styles** — concise, step-by-step, beginner-friendly, detailed, and Socratic.
- **Prompt preview** — inspect the assembled prompt before generating an answer.
- **Two run modes** — built-in demo mode (no key needed) or live OpenAI API mode.

## 1. Requirements
- Python 3.10 or newer
- Git
- Internet connection only for installing dependencies and live API calls

## 2. Run locally

### Windows (PowerShell)
```powershell
cd smart_qa_assistant
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

### macOS / Linux
```bash
cd smart_qa_assistant
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```
Open the local URL printed by Streamlit (normally http://localhost:8501). You can use demo mode immediately without an API key.

## 3. Enable live AI answers (optional)
1. Create an API key in your OpenAI account.
2. In the app sidebar, paste it into **OpenAI API key**.
3. Keep the model as `gpt-4o-mini` or enter a model available to your account.
4. Do not commit API keys. The app uses the key only for the current run; clear it when finished.

## 4. Test the project
Run unit tests from the project folder:
```bash
python -m unittest discover -s tests -v
```
Expected: 4 tests pass. The tests validate role instructions, few-shot inclusion, empty examples, and demo output.

## 5. Connect this project to your Git repository

### Option A — New GitHub repository
1. Create an empty repository on GitHub (do not initialize it with a README if you plan to push this folder).
2. Extract this ZIP file.
3. Open a terminal in the extracted `smart_qa_assistant` folder.
4. Run:
```bash
git init
git add .
git commit -m "Initial commit: Smart Q&A Assistant"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```
Replace the URL with your repository URL.

### Option B — Existing repository
Copy the `app.py`, `prompt_engine.py`, `requirements.txt`, `tests/`, `.gitignore`, and README into your repository (or into a new subfolder). Then:
```bash
git add .
git commit -m "Add Smart Q&A Assistant project"
git push
```
If the repository already has a Python app, avoid overwriting its existing dependency or README files; merge the needed entries.

## 6. Verify after cloning
```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python -m streamlit run app.py
```

## Project structure
```text
smart_qa_assistant/
├── app.py
├── prompt_engine.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
└── tests/
    └── test_prompt_engine.py
```

## Notes
- Demo mode is intentionally a predictable sample, not a real language model.
- Live AI mode requires a valid API key and may incur API usage charges.
- Never upload `.env`, API keys, passwords, or other secrets to Git.

Fahamu AI 254

Offline AI Assistant for the Kenya Data Protection Act, 2019

Fahamu AI 254 is an offline Retrieval-Augmented Generation (RAG) system that enables organizations, legal professionals, students, compliance officers, and Data Protection Officers (DPOs) to interact with the Kenya Data Protection Act using natural language.

Unlike cloud-based AI assistants, Fahamu AI 254 runs entirely on a local machine, ensuring sensitive organizational data never leaves the user's environment.

Features

* Ask questions about the Kenya Data Protection Act in plain English.
* Retrieval-Augmented Generation (RAG) for accurate, document-grounded answers.
* Fully offline operation using local AI models.
* Fast document retrieval through vector embeddings.
* Privacy-first architecture suitable for organizations handling sensitive data.
* Extensible knowledge base for additional regulations and policies.
* Simple web interface for interacting with the assistant.

#Technology Stack

* Python
* FastAPI
* Ollama
* ChromaDB / Vector Database
* Sentence Transformers
* HTML / CSS / JavaScript

Project Structure

```text
app/
docs/
ingest/
knowledge_base/
tests/
ui/
run.py
requirements.txt
README.md
```
Installation

Clone the repository:

```bash
git clone https://github.com/Waimonde/fahamuai254.git
cd fahamuai254
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python run.py
```

Use Cases

* Organizations implementing the Kenya Data Protection Act.
* Data Protection Officers (DPOs).
* Compliance teams.
* Legal practitioners.
* Universities and training institutions.
* Students learning data privacy and compliance.

Future Enhancements

* PDF upload and analysis.
* Multi-document search.
* Citation-aware responses.
* Voice interaction.
* Multi-language support.
* Additional Kenyan legislation integration.
* User authentication and audit logs.

License

This project is intended for educational, research, and organizational compliance purposes. Please ensure that any legal guidance obtained from the system is verified against the official Kenya Data Protection Act and related regulations.

Author

**David Maina Waimonde**

Built with ❤️ in Kenya to make data protection knowledge more accessible through Artificial Intelligence.

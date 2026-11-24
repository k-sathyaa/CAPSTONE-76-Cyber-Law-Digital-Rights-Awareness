# CAPSTONE 76 — Cyber Law and Digital Rights Awareness (India)

A responsive Flask web application that introduces students to cyber law, privacy, constitutional digital rights, common cyber offences, copyright and online safety in India.

## Features
- Home dashboard with project overview and quick navigation
- Learning hub with six topic modules
- Interactive 8-question quiz with score and explanations
- Personal cyber-safety checklist with progress indicator
- Official reporting and reference links
- Responsive layout for desktop and mobile

## Technology stack
- Python 3
- Flask
- HTML5, CSS3 and vanilla JavaScript
- JSON files for learning content and quiz questions

## Run locally (Windows)
1. Install Python 3.10 or newer.
2. Extract the ZIP and open this folder in VS Code.
3. Open Terminal in VS Code.
4. Create a virtual environment:
   ```powershell
   py -m venv .venv
   .venv\\Scripts\\activate
   ```
5. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
6. Start the application:
   ```powershell
   python app.py
   ```
7. Open `http://127.0.0.1:5000` in your browser.

## Project structure
```text
CAPSTONE_76_Cyber_Law_Digital_Rights_India/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   ├── topics.json
│   ├── quiz.json
│   └── resources.json
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── learn.html
│   ├── quiz.html
│   ├── resources.html
│   ├── safety.html
│   └── 404.html
└── static/
    ├── app.js
    └── style.css
```

## Important legal accuracy note
This is an awareness/academic project, not legal advice. Laws, rules, commencement dates, notifications and reporting processes may change. The Digital Personal Data Protection Act, 2023 has phased commencement/implementation details; do not treat every provision as operational without checking the latest Gazette notifications and official MeitY material. The Information Technology Act, 2000 has also been amended over time. Verify current consolidated legislation from India Code before using this project for legal decisions.

## Suggested official references
- India Code: https://www.indiacode.nic.in/
- Ministry of Electronics and Information Technology: https://www.meity.gov.in/
- National Cyber Crime Reporting Portal: https://cybercrime.gov.in/
- CERT-In: https://www.cert-in.org.in/
- Ministry of Home Affairs: https://www.mha.gov.in/
- Supreme Court of India, *K.S. Puttaswamy v. Union of India* (2017), privacy judgment: https://www.sci.gov.in/

## Suggested future enhancements
- Admin panel to add/edit modules
- Database-backed quiz history and user accounts
- Tamil language toggle
- Accessibility review and screen-reader testing
- Automated tests and deployment to a hosting platform

# Smart Print Spooler — Intelligent Document Queue Manager

An operating-system-inspired print queue simulator demonstrating job scheduling, priority management, and queue operations.

**Built by Swaraj Sonalkar**

## Overview

Smart Print Spooler is an academic software project based on Operating System concepts.

It demonstrates how a print queue can manage multiple document jobs using priority-based scheduling and job state management.

The application simulates printing operations without connecting to a physical printer.

## Features

- Add document jobs
- Priority-based job management
- Five priority levels
- Queue visualization
- Pause jobs
- Resume jobs
- Simulated printing
- Cancel jobs
- Persistent job storage
- SQLite database integration

## Operating System Concepts

- Process scheduling
- Queue management
- Priority scheduling
- Job states
- Resource management
- Database-backed state persistence

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend |
| Flask | Web framework |
| SQLite | Database |
| HTML5 | Structure |
| CSS3 | Styling |
| JavaScript | Frontend interaction |

## Project Structure

```text
SMART-PRINT-SPOOLER/
├── app.py
├── spooler.db
├── requirements.txt
├── README.md
└── static/
    ├── index.html
    ├── style.css
    └── app.js
```

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/swarajsonalkar-web/Smart-Print-Spooler.git
cd Smart-Print-Spooler
```

**2. Create a virtual environment**

```bash
python -m venv .venv
```

**3. Activate the environment**

```bash
source .venv/bin/activate
```

**4. Install dependencies**

```bash
pip install -r requirements.txt
```

**5. Run the application**

```bash
python app.py
```

Open: http://127.0.0.1:5005

## Future Improvements

- Real printer integration
- Advanced scheduling algorithms
- First-Come-First-Served scheduling
- Shortest Job First scheduling
- Priority scheduling comparisons
- Queue performance analytics
- Print history and reports

## Developer

**Swaraj Sonalkar**

GitHub: https://github.com/swarajsonalkar-web

Email: swarajsonalkar99@gmail.com

---

*Exploring Operating System concepts through practical software development.*

Make a separate static in oroject directory and then paste the html,css and javascript file

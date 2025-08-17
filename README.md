# Week 2 Bootcamp Projects

Welcome to the **Week 2 Bootcamp** repository! 🎉
This repository contains Python scripts that focus on **file handling, automation, and log analysis** to strengthen real-world programming skills.

---

## 📂 Repository Contents

| File/Directory             | Description                                                                 |
| -------------------------- | --------------------------------------------------------------------------- |
| `access.log`               | Sample log file used for testing log analysis.                              |
| `bulk_rename.py`           | Script to rename multiple files in a directory based on a given pattern.    |
| `bulk_rename_scheduler.py` | Automates bulk file renaming at scheduled intervals.                        |
| `log_analyzer.py`          | Parses `access.log` and generates summary reports in JSON and text formats. |
| `log_results.json`         | Example structured output generated from `log_analyzer.py`.                 |
| `log_results.txt`          | Human‑readable text report from the log analyzer.                           |
| `weather.csv`              | Sample dataset containing weather data.                                     |
| `weather_report.py`        | Generates a report using data from `weather.csv`.                           |

---

## ⚙️ Setup & Requirements

* **Python Version**: Python 3.x
* **Libraries**: Standard Python libraries (`os`, `re`, `csv`, `json`, `datetime`, etc.)

### Clone the Repository

```bash
git clone https://github.com/azeemasabir/week2-bootcamp.git
cd week2-bootcamp
```

### Run Scripts

```bash
python bulk_rename.py
python bulk_rename_scheduler.py
python log_analyzer.py
python weather_report.py
```

---

## 📝 Example Use Cases

* **Bulk File Renaming**: Quickly rename multiple files in a directory with consistent naming conventions.
* **Scheduled Renaming**: Automate renaming tasks to run at regular time intervals.
* **Log Analysis**: Parse server or application logs (`access.log`) and export results in JSON or text.
* **Weather Report**: Summarize data (like averages or statistics) from a weather dataset.

---

## 🧪 Running Tests

If test cases are included, run them using:

```bash
pytest
```

*or*

```bash
python -m unittest discover
```

---

## 🎯 Project Goals

* Strengthen understanding of **automation** and **scheduling** in Python.
* Practice **log parsing** and **report generation**.
* Work with **file handling** (CSV, JSON, plain text).
* Build practical scripts that simulate real-world tasks.

---

## 🤝 Contribution

Contributions, improvements, and suggestions are always welcome! Fork this repository, open an issue, or submit a pull request.



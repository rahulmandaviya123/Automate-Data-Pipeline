# Automate Data Pipeline in Python

## 📌 Project Overview
This project demonstrates how to build an **automated data pipeline in Python**.  
It covers file handling, data processing, and archiving to streamline workflow.

## 🚀 Features
- Reads and processes CSV files
- Handles processed files automatically
- Archives old files
- Fully automated workflow

## 🛠️ Tech Stack
- Python 3.x
- Pandas
- OS, Glob, Shutil

## 📂 Project Structure
```
Automate-Data-Pipeline/
│── notebooks/                     # Jupyter notebooks
│── src/                           # Source Python scripts
│── data/                          # Sample input/output data
│── README.md
│── requirements.txt
│── .gitignore
```

## ⚙️ Installation
1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/automate-data-pipeline.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Usage
Run the pipeline:
```bash
python src/pipeline.py
```

Or explore the Jupyter notebook in:
```
notebooks/Automate_Data_pipeline-2.ipynb
```

## 📌 Next Steps
- Add scheduling with `cron` or `Airflow`
- Extend to handle more file types
- Add cloud storage integration

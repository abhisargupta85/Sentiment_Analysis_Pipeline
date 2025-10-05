# Sentiment_Analysis_Project
Modular, full-stack data pipeline for IMDB review sentiment analysis.

# Modular Sentiment Analysis Pipeline: IMDB Movie Reviews 

## Project Overview
This project demonstrates a professional, modular data science pipeline built for sentiment analysis. It showcases strong architectural principles by strictly separating concerns into distinct Python modules (Data, NLP Processing, Execution) and using a specialized tool (R) for final reporting and visualization.

The analysis is performed on a sampled subset of the large IMDB Movie Reviews dataset.

## Project Architecture (Separation of Concerns) 
The workflow is orchestrated by `main_execution.py` and follows a clear contract between layers:

| File | Role | Technologies | I/O Contract |
| :--- | :--- | :--- | :--- |
| **`data_setup.py`** | Data Ingestion & Filtering | Python, Pandas | Loads raw CSV, returns DataFrame (`review_id`, `review_text`) |
| **`nlp_pipeline.py`** | Core Model/Scoring Layer | Python, RegEx, Lexicon | Accepts DataFrame, returns DataFrame (`...`, `compound`, `sentiment`) |
| **`main_execution.py`** | Orchestrator & Exporter | Python, datetime | Runs 1 & 2, exports final results to a single `.csv` file. |
| **`reporting.R`** | Visualization & Reporting | R, Tidyverse (ggplot2, dplyr) | Loads `.csv` file, produces statistical summary and PNG plot. |

## Execution Steps

1.  **Clone the Repository:** Clone this project to your local machine.
2.  **Ensure Data is Present:** Confirm `IMDB Dataset.csv` is in the root directory.
3.  **Run Python Pipeline:** Execute the main script to process data and generate results.
    ```bash
    python main_execution.py
    ```
4.  **Run R Reporting:** Open the project directory in RStudio or run the R script from an R terminal.
    ```R
    source("reporting.R")
    ```
## Dataset Source

Dataset: https://www.kaggle.com/code/nourhankarm/sentiment-analysis-of-movie-reviews-imdb-dataset/input

---

##  Insights & Future Work

### 1. Design Constraints & Workarounds (Critical Thinking)
The original design relied on the **VADER** lexicon from NLTK, a general-purpose sentiment model. Due to an environmental network constraint (NLTK download failure during execution), the VADER dependency was replaced with a **highly simplified, hardcoded, rule-based lexicon** to maintain the integrity of the architecture.

**Impact:** This temporary measure resulted in the majority of reviews being classified as "Neutral" (approx. 99.6%). This skewed result is a predictable artifact of the simple model, showcasing the importance of choosing a robust, production-ready NLP approach.

### 2. Future Work & Production Scaling

* **NLP Model Improvement (Accuracy):**
    * Replace the temporary lexicon in `nlp_pipeline.py` with a **fine-tuned transformer model (e.g., DistilBERT or RoBERTa)** specifically trained on the IMDB dataset for state-of-the-art accuracy.
* **Data Source Improvement (Scalability):**
    * Refactor `data_setup.py` to ingest data from a real-time, external source, such as a $\text{PostgreSQL}$ database query or a $\text{Kafka}$ topic, instead of reading a static local file.
* **Orchestration:**
    * Integrate the entire workflow into a scheduling tool like $\text{Apache Airflow}$ to manage dependencies and schedule automated daily reports.

---

### 3. Other Core Files (Placeholders)

| File | Content |
| :--- | :--- |
| **`.gitignore`** | Exclude generated files like `sentiment_results_*.csv`, `sentiment_distribution_report.png`, and environment folders (`__pycache__`, `.venv`). |
| **`requirements.txt`**| `pandas`, `nltk`, `sqlite3` (built-in) |

**NOTE:** This project uses publicly available data for educational and analytical purposes. No personal data is stored or processed beyond what is publicly accessible.

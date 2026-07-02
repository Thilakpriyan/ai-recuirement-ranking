# AI Recruitment Ranking System

An AI-powered candidate ranking system developed for the **Redrob AI Hiring Challenge**.

Traditional recruitment systems rely heavily on keyword matching, often overlooking highly qualified candidates whose profiles don't exactly match the wording of a job description. This project addresses that limitation by combining recruiter-inspired scoring, semantic search, and transformer-based reranking to identify the best candidates for a role.

The system analyzes the complete candidate profile—including experience, technical skills, career history, behavioral signals, GitHub activity, recruiter engagement, and semantic relevance—to produce a ranked shortlist that closely resembles how an experienced recruiter evaluates candidates.

---
# 🚀 AI Recruitment Ranking System

An AI-powered candidate ranking system developed for the **Redrob AI Hiring Challenge**.

---

## 🛠️ Tech Stack

<p align="center">

<img src="https://skillicons.dev/icons?i=python" height="60"/>

<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original.svg" width="60"/>

<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/numpy/numpy-original.svg" width="60"/>

<img src="https://huggingface.co/front/assets/huggingface_logo.svg" width="60"/>

<img src="https://upload.wikimedia.org/wikipedia/commons/7/7c/Faiss_logo.png" width="70"/>

</p>

<p align="center">

<img src="https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python"/>

<img src="https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=for-the-badge&logo=pandas"/>

<img src="https://img.shields.io/badge/NumPy-Numerical-013243?style=for-the-badge&logo=numpy"/>

<img src="https://img.shields.io/badge/FAISS-Vector%20Search-orange?style=for-the-badge"/>

<img src="https://img.shields.io/badge/SentenceTransformers-NLP-yellow?style=for-the-badge"/>

<img src="https://img.shields.io/badge/CrossEncoder-Reranking-green?style=for-the-badge"/>

<img src="https://img.shields.io/badge/Git-GitHub-F05032?style=for-the-badge&logo=git"/>

</p>
# Project Highlights

- Hybrid AI candidate ranking pipeline
- Recruiter-inspired structured scoring system
- Semantic candidate retrieval using Sentence Transformers
- FAISS vector indexing for efficient similarity search
- Cross-Encoder reranking for contextual relevance
- Automatic candidate filtering based on hiring constraints
- Intelligent weighted score fusion
- Automatic submission file generation
- Modular and production-oriented project structure

---

# Problem Statement

Recruiters review hundreds or thousands of candidate profiles for every role.

Traditional Applicant Tracking Systems (ATS) primarily rely on keyword matching, which often fails to recognize strong candidates whose experience is semantically relevant but described differently.

This project aims to build an AI-driven recruitment engine capable of:

- Understanding the job description
- Evaluating complete candidate profiles
- Performing semantic candidate retrieval
- Ranking candidates using multiple signals
- Producing recruiter-quality recommendations

---

# Complete Pipeline

```
                 Job Description
                        │
                        ▼
          JD Feature Extraction
                        │
                        ▼
            Candidate Dataset
                        │
                        ▼
          Structured Candidate Filtering
                        │
                        ▼
        Recruiter Score Calculation
                        │
                        ▼
          Top Candidate Selection
                        │
                        ▼
      Sentence Transformer Embeddings
                        │
                        ▼
            FAISS Semantic Search
                        │
                        ▼
         Cross Encoder Re-ranking
                        │
                        ▼
      Hybrid Weighted Score Fusion
                        │
                        ▼
          Final Candidate Ranking
                        │
                        ▼
            submission.csv
```

---

# Project Architecture

```
src/

├── features/
│   ├── candidate_features.py
│   └── jd_features.py
│
├── models/
│   ├── embedding_model.py
│   └── cross_encoder.py
│
├── pipeline/
│   ├── build_index.py
│   └── run_pipeline.py
│
├── services/
│   ├── filter_service.py
│   └── ranking_service.py
│
├── loader.py
├── retrieval.py
├── config.py
└── utils.py
```

---

# Project Workflow

## Phase 1 — Data Loading

Objective:

Load the job description and candidate dataset.

Implemented:

- Candidate JSONL loader
- Job Description loader
- Dataset preprocessing

Deliverable:

- Candidate DataFrame
- Job Description text

---

## Phase 2 — Job Description Understanding

Objective:

Extract recruiter-relevant hiring requirements.

Features extracted:

- Experience range
- Required technical skills
- Work mode
- Startup preference
- Leadership requirements
- Relocation preference

Deliverable:

Structured JD feature dictionary.

---

## Phase 3 — Candidate Filtering

Objective:

Reduce search space before semantic retrieval.

Filtering criteria:

- Experience
- Open to work
- Profile completeness
- GitHub activity
- Minimum skill overlap

Deliverable:

High-quality candidate pool.

---

## Phase 4 — Recruiter Scoring

Objective:

Rank candidates using structured recruiter signals.

Signals considered:

- Experience match
- Skill overlap
- GitHub activity
- Profile completeness
- Recruiter response rate
- Skill assessment scores

Deliverable:

Recruiter score for every filtered candidate.

---

## Phase 5 — Semantic Retrieval

Objective:

Retrieve candidates whose profiles are semantically similar to the job description.

Implementation:

- Sentence Transformer embeddings
- FAISS vector search
- Dense semantic retrieval

Deliverable:

Top semantically relevant candidates.

---

## Phase 6 — Cross Encoder Re-ranking

Objective:

Improve semantic ranking using deep contextual comparison.

Implementation:

Cross Encoder evaluates:

(Job Description, Candidate Profile)

instead of independent embeddings.

Deliverable:

Context-aware relevance score.

---

## Phase 7 — Hybrid Score Fusion

Objective:

Combine all ranking signals.

Final score consists of:

- Recruiter Score
- Semantic Similarity
- Cross Encoder Score

Normalized scores are combined using weighted ranking.

Deliverable:

Final recruiter-quality ranking.

---

# Technologies Used

## Programming

- Python 3

## Machine Learning

- Sentence Transformers
- Cross Encoder
- Transformers

## Vector Search

- FAISS

## Data Processing

- Pandas
- NumPy

## Utilities

- python-docx

---

# Installation

Clone repository

```bash
git clone https://github.com/Thilakpriyan/ai-recuirement-ranking.git

cd ai-recuirement-ranking
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Run Project

```bash
python app.py
```

---

# Output

The pipeline automatically generates:

```
output/

submission.csv
```

Submission format:

```
candidate_id
rank
score
reasoning
```

---

# Repository Structure

```
AI-Recruitment-Ranking/

│
├── data/
├── models/
├── output/
├── src/
│
├── app.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Key Features

- Recruiter-inspired ranking
- Hybrid AI retrieval
- Semantic search
- Transformer reranking
- Modular architecture
- Easily extensible pipeline
- Production-style code organization

---

# Future Improvements

- LLM-generated candidate reasoning
- Dynamic score optimization
- Learning-to-Rank models
- GPU batch inference
- Multi-job ranking support
- Resume PDF parsing
- Explainable AI dashboards
- REST API deployment

---

# Author

**Thilak Priyan**

AI Recruitment Ranking System

Developed as part of the **Redrob AI Hiring Challenge**.

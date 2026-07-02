from pathlib import Path

# ==========================
# Project Directories
# ==========================

ROOT_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = ROOT_DIR / "data"
MODEL_DIR = ROOT_DIR / "models"
OUTPUT_DIR = ROOT_DIR / "output"

# ==========================
# Dataset Files
# ==========================

CANDIDATE_FILE = DATA_DIR / "candidates.jsonl"
JOB_DESCRIPTION_FILE = DATA_DIR / "job_description.docx"

# ==========================
# Embedding Cache
# ==========================

EMBEDDINGS_FILE = MODEL_DIR / "candidate_embeddings.npy"
ID_FILE = MODEL_DIR / "candidate_ids.npy"
FAISS_INDEX = MODEL_DIR / "candidate.index"

# ==========================
# Model Names
# ==========================

EMBEDDING_MODEL = "BAAI/bge-large-en-v1.5"

RERANK_MODEL = "cross-encoder/ms-marco-MiniLM-L-6-v2"

TOP_K = 1000
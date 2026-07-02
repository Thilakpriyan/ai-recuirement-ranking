import json
from pathlib import Path

import pandas as pd
from docx import Document

from src.config import CANDIDATE_FILE, JOB_DESCRIPTION_FILE


class DataLoader:

    @staticmethod
    def load_candidates():

        candidates = []

        with open(CANDIDATE_FILE, "r", encoding="utf-8") as f:

            for line in f:
                candidates.append(json.loads(line))

        return pd.DataFrame(candidates)

    @staticmethod
    def load_job_description():

        doc = Document(JOB_DESCRIPTION_FILE)

        text = []

        for para in doc.paragraphs:
            text.append(para.text)

        return "\n".join(text)
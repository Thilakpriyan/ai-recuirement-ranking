import faiss
import numpy as np

from tqdm import tqdm

from src.loader import DataLoader
from src.models.embedding_model import EmbeddingModel
from src.utils import build_candidate_text
from src.config import (
    EMBEDDINGS_FILE,
    ID_FILE,
    FAISS_INDEX,
)

BATCH_SIZE = 512

print("Loading candidates...")

df = DataLoader.load_candidates().head(5000 )

print(f"Loaded {len(df)} candidates")

model = EmbeddingModel()

all_embeddings = []
all_ids = []

index = None

for start in tqdm(range(0, len(df), BATCH_SIZE)):

    end = min(start + BATCH_SIZE, len(df))

    batch = df.iloc[start:end]

    texts = []

    ids = []

    for _, row in batch.iterrows():

        candidate = row.to_dict()

        texts.append(
            build_candidate_text(candidate)
        )

        ids.append(
            candidate["candidate_id"]
        )

    embeddings = model.encode(texts)

    embeddings = embeddings.astype("float32")

    if index is None:

        index = faiss.IndexFlatIP(
            embeddings.shape[1]
        )

    index.add(embeddings)

    all_embeddings.append(embeddings)

    all_ids.extend(ids)

print("Saving embeddings...")

embeddings = np.vstack(all_embeddings)

np.save(
    EMBEDDINGS_FILE,
    embeddings
)

np.save(
    ID_FILE,
    np.array(all_ids)
)

print("Saving FAISS index...")

faiss.write_index(
    index,
    str(FAISS_INDEX)
)

print("Index successfully created.")
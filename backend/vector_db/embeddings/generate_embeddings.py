# import the libraries
from sentence_transformers import SentenceTransformer
import numpy as np
from sample_text import SAMPLE_TEXT

print("OmniBrain- Embedding Generator")


print("\n Embedding Model Loading...")
model= SentenceTransformer("all-MiniLM-L6-v2")
print("\n Model Loaded")


print("\n Generating Embeddings..")
embeddings= model.encode(SAMPLE_TEXT)
print("\n Embedding Generated")


print("\n Embedding Shape:", embeddings.shape)
print("\n Embedding Dimension:", len(embeddings[0]))


for i, sentence in enumerate(SAMPLE_TEXT):
    print(f"Sentence {i+1}:")
    print(sentence)

    print("First 10 vector value:")
    print(embeddings[i][:10])

# save embedding
np.save("embeddings.npy", embeddings)

print("Embedded Saved successfully")
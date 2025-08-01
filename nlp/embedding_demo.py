# === ALL-IN-ONE: Wikipedia Grab + Embedding Playground ===

import wikipedia
from gensim.models import KeyedVectors
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import re

# 1. Grab Notes from Wikipedia
wikipedia.set_lang("en")
page_title = "History of cricket"
page = wikipedia.page(page_title)
full_text = page.content
notebook_text = [para.strip() for para in full_text.split('\n') if para.strip()]

print(f"\nGrabbed {len(notebook_text)} paragraphs from Wikipedia page: '{page_title}'")
print("\nFirst 3 paragraphs:")
for para in notebook_text[:3]:
    print("-", para)

# 2. Word Embeddings (using GloVe, change path if needed)
print("\n=== WORD EMBEDDINGS EXAMPLES ===")
word_vec_path = r'C:\Users\mohan\OneDrive\Desktop\Gen AI\nlp\glove.twitter.27B.25d.w2v.txt'
word_model = KeyedVectors.load_word2vec_format(word_vec_path, binary=False)
unique_words = set()
for sent in notebook_text:
    for word in re.findall(r"\b\w+\b", sent.lower()):
        unique_words.add(word)
for word in ["cricket", "england", "test", "international", "bat"]:
    if word in unique_words and word in word_model:
        print(f"\nWord: {word}")
        print(f"Vector (first 5): {word_model[word][:5]}")
        print("Top 3 similar words:", word_model.most_similar(word, topn=3))

# 3. Sentence Embeddings
print("\n=== SENTENCE EMBEDDINGS ===")
sent_model = SentenceTransformer('all-MiniLM-L6-v2')
sentence_embeddings = sent_model.encode(notebook_text)
for i, sent in enumerate(notebook_text[:3]):
    print(f"Sentence {i+1} (first 5 dims): {sentence_embeddings[i][:5]}")

# 4. Document Embedding (mean of all sentences)
print("\n=== DOCUMENT EMBEDDING ===")
doc_embedding = np.mean(sentence_embeddings, axis=0)
print("Document embedding (first 5 dims):", doc_embedding[:5])

# 5. Semantic Search (most similar sentence to a query)
print("\n=== SEMANTIC SEARCH ===")
query = "Who played the first Test match?"
query_vec = sent_model.encode([query])[0]
sims = cosine_similarity([query_vec], sentence_embeddings)[0]
best_idx = np.argmax(sims)
print(f"Query: {query}")
print(f"Most similar sentence:\n{notebook_text[best_idx]} (Score: {sims[best_idx]:.3f})")

# 6. (Optional) Vector Database Search with Chroma
try:
    import chromadb
    print("\n=== CHROMA VECTOR SEARCH ===")
    client = chromadb.Client()
    collection = client.create_collection("cricket_paragraphs")
    ids = [f"para_{i}" for i in range(len(notebook_text))]
    collection.add(
        embeddings=sentence_embeddings.tolist(),
        ids=ids,
        documents=notebook_text
    )
    query_embedding = sent_model.encode(["Ashes series"])[0].tolist()
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=2,
        include=["documents", "distances"]
    )
    for doc, dist in zip(results['documents'][0], results['distances'][0]):
        print(f"Chroma found: \"{doc}\" (Distance: {dist:.4f})")
except Exception as e:
    print("ChromaDB not available or not installed:", e)

# 7. Visualization
print("\n=== SENTENCE EMBEDDING VISUALIZATION (PCA) ===")
pca = PCA(n_components=2)
reduced = pca.fit_transform(sentence_embeddings)
plt.figure(figsize=(8,6))
plt.scatter(reduced[:, 0], reduced[:, 1])
for i, txt in enumerate(notebook_text[:10]):  # Show numbers for first 10 only
    plt.text(reduced[i, 0] + 0.01, reduced[i, 1] + 0.01, f"{i+1}", fontsize=9)
plt.title("First 10 Sentence Embeddings Visualization (PCA)")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.tight_layout()
plt.show()

# 📦 Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer

# 📥 Download tokenizer if not already
nltk.download('punkt')

# 📘 Sample dataset of 40–50 product reviews
reviews = [
    "I love this phone! Great battery life and camera.",
    "Battery drains too fast. Not satisfied.",
    "Amazing product. Works flawlessly and very durable.",
    "Not worth the price. Too expensive for the features.",
    "Excellent sound quality and easy to pair.",
    "Worst purchase ever. Stopped working in a week.",
    "Good value for money. Very satisfied with performance.",
    "Product arrived damaged. Disappointed.",
    "The design is sleek and performance is top-notch.",
    "Terrible customer service experience.",
    "Absolutely love the screen resolution!",
    "Buttons are hard to press. Not user-friendly.",
    "Very responsive and fast. Happy with the speed.",
    "Not as described. Missing accessories.",
    "Superb build quality and premium feel.",
    "Overheats quickly. Can’t be used for gaming.",
    "Received a fake product. Beware.",
    "Great for everyday tasks. Lightweight and powerful.",
    "Color is different from the pictures shown.",
    "Quick delivery and neatly packed.",
    "Too bulky. Not travel friendly.",
    "Absolutely useless. Don’t buy at all.",
    "Met all my expectations. Very satisfied!",
    "The battery swells up quickly. Dangerous.",
    "Keyboard lights are too dim in the dark.",
    "Slow startup time. Needs improvement.",
    "Great value for money. Highly recommended!",
    "Build feels cheap. Not worth it.",
    "Very intuitive interface. Loved it!",
    "Came with pre-installed bloatware.",
    "The charging port became loose in a week.",
    "Impressed with the speed and display quality.",
    "Camera quality is decent for the price.",
    "Speaker sounds low. Can’t hold calls.",
    "Amazing for students. Budget friendly.",
    "Touch response is great.",
    "Display is crisp and vivid.",
    "Buttons feel solid and clicky.",
    "Packaging was poor. Product was safe though.",
    "Perfect size and handy to use.",
    "Device lags occasionally but manageable.",
]

# ✅ Step 1: Tokenization
all_tokens = []
for review in reviews:
    tokens = word_tokenize(review.lower())  # Convert to lowercase and tokenize
    all_tokens.extend(tokens)

# ✅ Step 2: Frequency Count
token_freq = Counter(all_tokens)
top_10_words = token_freq.most_common(10)

# ✅ Step 3: Bag of Words (BoW)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(reviews)
bow_df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

# ✅ Step 4: N-Grams (Bigrams)
bigrams = list(ngrams(all_tokens, 2))
bigram_freq = Counter(bigrams)
top_10_bigrams = bigram_freq.most_common(10)

# ✅ Step 5A: Bar Chart – Top 10 Words
words, freqs = zip(*top_10_words)
plt.figure(figsize=(10, 6))
plt.bar(words, freqs, color='skyblue')
plt.title("Top 10 Most Frequent Words")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ✅ Step 5B: Word Cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(" ".join(all_tokens))
plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Word Cloud of Product Reviews")
plt.show()

# ✅ Step 5C: Bar Chart – Top 10 Bigrams
bigram_labels = [' '.join(b) for b, _ in top_10_bigrams]
bigram_counts = [count for _, count in top_10_bigrams]

plt.figure(figsize=(10, 6))
plt.bar(bigram_labels, bigram_counts, color='orange')
plt.title("Top 10 Most Frequent Bigrams")
plt.xlabel("Bigrams")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

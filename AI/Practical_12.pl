# Experiment 12: Implementation of Text Preprocessing in Python
# Environment: Python 3.x

import string
import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer


# Download required NLTK corpora and models
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)


def preprocess_text(raw_text):

    print("=====================================================")
    print("                 RAW INPUT TEXT")
    print("=====================================================")

    print(raw_text)

    print("\n" + "=" * 53)

    print("           STEP-BY-STEP PREPROCESSING PIPELINE")

    print("=" * 53)

    # Step 1: Lowercase Conversion
    lowercased_text = raw_text.lower()

    print(
        f"\n1. Lowercase Conversion:\n"
        f" {lowercased_text}"
    )

    # Step 2: Removal of Punctuation
    clean_text = lowercased_text.translate(
        str.maketrans(
            '',
            '',
            string.punctuation
        )
    )

    print(
        f"\n2. Punctuation Removal:\n"
        f" {clean_text}"
    )

    # Step 3: Word Tokenization
    tokens = word_tokenize(clean_text)

    print(
        f"\n3. Tokenization:\n"
        f" {tokens}"
    )

    # Step 4: Stop Word Removal
    stop_words = set(
        stopwords.words('english')
    )

    filtered_tokens = [
        w for w in tokens
        if w not in stop_words
    ]

    print(
        f"\n4. Stop Word Removal:\n"
        f" {filtered_tokens}"
    )

    # Step 5: Stemming
    stemmer = PorterStemmer()

    stemmed_words = [
        stemmer.stem(w)
        for w in filtered_tokens
    ]

    print(
        f"\n5. Stemming (Porter Stemmer):\n"
        f" {stemmed_words}"
    )

    # Step 6: Lemmatization
    lemmatizer = WordNetLemmatizer()

    lemmatized_words = [
        lemmatizer.lemmatize(w)
        for w in filtered_tokens
    ]

    print(
        f"\n6. Lemmatization (WordNet Lemmatizer):\n"
        f" {lemmatized_words}"
    )

    # Final Cleaned Output
    final_output = " ".join(
        lemmatized_words
    )

    print("\n" + "=" * 53)

    print("             FINAL PREPROCESSED TEXT")

    print("=" * 53)

    print(final_output)


if __name__ == "__main__":

    # Sample sentence
    sample_text = (
        "Artificial Intelligence (AI) is transforming the world! "
        "The algorithms are running, studying, and learning "
        "better models from data."
    )

    preprocess_text(sample_text)
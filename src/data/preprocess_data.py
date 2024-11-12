import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def clean_text(text: str) -> str:
    """
    Clean text data by removing URLs, special characters, and stopwords.
    """
    text = re.sub(r'http\S+', '', text)             # Remove URLs
    text = re.sub(r'@\w+', '', text)                # Remove mentions
    text = re.sub(r'[^a-zA-Z\s]', '', text)         # Remove non-ASCII
    text = text.lower()                             # Convert to lowercase
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocess raw dataframe and return cleaned dataframe.
    """
    df['cleaned_text'] = df['text'].apply(clean_text)
    return df

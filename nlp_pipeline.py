import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import re

# Download resources (uncomment and run once in the environment
import nltk

# Download only if not already present
nltk.download('vader_lexicon')
nltk.download('punkt')



# Initialize the VADER analyzer outside the function for efficiency
sia = SentimentIntensityAnalyzer()

def preprocess_and_score(df, text_column='review_text'):
    """
    Cleans the text data and applies the VADER sentiment analysis model.

    Args:
        df (pd.DataFrame): DataFrame containing the text data.
        text_column (str): Name of the column with review text.

    Returns:
        pd.DataFrame: Original DataFrame with 'compound' score and 'sentiment' label added.
    """

    def analyze_sentiment(text):
        if not isinstance(text, str):
            return {'compound': 0.0, 'sentiment': 'Neutral'}

        # Step 1: Basic Cleaning (Remove noise and lowercase)
        # VADER works well without heavy stop word/stemming,
        # but basic cleaning is necessary.
        cleaned_text = re.sub(r'[^\w\s]', '', text).lower()

        # Step 2: Get VADER scores
        scores = sia.polarity_scores(cleaned_text)
        compound_score = scores['compound']

        # Step 3: Classify Sentiment
        # Standard classification thresholds for VADER
        if compound_score >= 0.05:
            sentiment = 'Positive'
        elif compound_score <= -0.05:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'

        return {'compound': compound_score, 'sentiment': sentiment}

    # Apply the function and expand results into new columns
    results = df[text_column].apply(analyze_sentiment).apply(pd.Series)

    # Combine original data with results
    final_df = pd.concat([df, results], axis=1)

    print("Sentiment scoring complete.")
    return final_df

if __name__ == '__main__':
    # Test data for local testing
    test_data = pd.DataFrame({
        'review_id': [10, 11, 12],
        'review_text': ["I love this!", "I hate that.", "It's just fine."],
    })
    scored_data = preprocess_and_score(test_data)
    print("\nSample Scored Data:")
    print(scored_data)
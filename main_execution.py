import pandas as pd
from datetime import datetime
from data_setup import setup_and_query_data
from nlp_pipeline import preprocess_and_score

def run_sentiment_analysis():
    """
    Main function to execute the full data science pipeline in Python.
    """
    print("--- Starting Sentiment Analysis Pipeline ---")
    
    # 1. DATA EXTRACTION (SQL Layer)
    raw_data = setup_and_query_data()
    print("\nRaw data ready for processing.")

    # 2. NLP PROCESSING & SCORING (NLP Layer)
    scored_data = preprocess_and_score(raw_data, text_column='review_text')
    print("\nSentiment analysis completed.")
    
    # Display a quick summary
    print("\n--- Final Results Summary (Python) ---")
    print(scored_data[['review_id', 'sentiment', 'compound']].head())
    print("\nSentiment Counts:")
    print(scored_data['sentiment'].value_counts())

    # 3 Export the final data for the R reporting step
    output_filename = f'sentiment_results_{datetime.now().strftime("%Y%m%d")}.csv'
    scored_data.to_csv(output_filename, index=False)
    print(f"\n--- Python Pipeline Finished ---")
    print(f"Results saved to: {output_filename}. Ready for R reporting.")

if __name__ == '__main__':
    run_sentiment_analysis()

import pandas as pd
import os

# --- Configuration ---
DATASET_FILE = 'IMDB Dataset.csv'
SAMPLE_SIZE = 5000  # Sample a manageable subset of 5,000 reviews from the 50,000 total

def setup_and_query_data(file_path=DATASET_FILE):
    """
    Reads the IMDB CSV dataset, creates a review_id, renames the text column,
    and samples a subset of the data to simulate a targeted SQL query.
    """
    if not os.path.exists(file_path):
        print(f"ERROR: Dataset file not found at '{file_path}'. Please ensure the file is in the project directory.")
        return pd.DataFrame()

    print(f"--- Data Extraction: Loading {file_path} ---")
    
    # 1. Load the data
    raw_df = pd.read_csv(file_path)

    # 2. Prepare/Rename columns to match the required format: 'review_id', 'review_text'
    # The 'review' column contains the text, which we rename to 'review_text'
    nlp_data = raw_df.rename(columns={'review': 'review_text'})
    
    # 3. Create a unique 'review_id' from the DataFrame index
    nlp_data.reset_index(inplace=True)
    nlp_data.rename(columns={'index': 'review_id'}, inplace=True)
    
    # 4. Simulate a targeted query by sampling a fixed number of rows
    # This is equivalent to filtering for a specific product or date range in a database
    if len(nlp_data) > SAMPLE_SIZE:
        # Use a random sample for general analysis
        final_data = nlp_data.sample(n=SAMPLE_SIZE, random_state=42)
        print(f"Extracted and sampled {SAMPLE_SIZE} records from the full {len(raw_df)} dataset.")
    else:
        final_data = nlp_data
        print(f"Extracted all {len(final_data)} records.")

    # Select only the required columns for the NLP pipeline
    return final_data[['review_id', 'review_text']]

if __name__ == '__main__':
    # Test the function if run directly
    data = setup_and_query_data()
    if not data.empty:
        print("\nSample of extracted data:")
        print(data.head())
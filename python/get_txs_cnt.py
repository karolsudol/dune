import os
import csv
import argparse
from datetime import datetime, timedelta
from dotenv import load_dotenv
from dune_client.types import QueryParameter
from dune_client.client import DuneClient
from dune_client.query import QueryBase

# Load environment variables
load_dotenv()

# Default parameters
DEFAULT_ADDRESSES = [
    "0x819f833BAe5deA66f0ABAb1E8723eBE105987e1C",
    "0xb7d1a295aad9e1816ec16c9835dc4373dadf646c"
]
DEFAULT_START_DATE = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
DEFAULT_END_DATE = datetime.now().strftime('%Y-%m-%d')

def execute_dune_query(addresses=DEFAULT_ADDRESSES, start_date=DEFAULT_START_DATE, end_date=DEFAULT_END_DATE):
    print(f"Executing Dune query for {len(addresses)} addresses from {start_date} to {end_date}...")
    
    query = QueryBase(
        name="Transaction Count Analysis",
        query_id=4607851,
        params=[
            QueryParameter.text_type(name="TransactionSenders", value=",".join(addresses)),
            QueryParameter.text_type(name="StartDate", value=start_date),
            QueryParameter.text_type(name="EndDate", value=end_date),
        ],
    )

    dune = DuneClient.from_env()
    results = dune.run_query_dataframe(query)
    
    print(f"Query executed successfully. Retrieved {len(results)} rows.")
    return results

def write_to_csv(df, filename='transaction_counts.csv'):
    print(f"Writing data to {filename}...")
    df.to_csv(filename, index=False)
    print(f"Data successfully written to {filename}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Extract transaction counts from Dune Analytics')
    parser.add_argument('--addresses', nargs='+', help='List of addresses to analyze')
    parser.add_argument('--start-date', help='Start date in YYYY-MM-DD format')
    parser.add_argument('--end-date', help='End date in YYYY-MM-DD format')
    
    args = parser.parse_args()
    
    # Print and use default values if no arguments provided
    if not any([args.addresses, args.start_date, args.end_date]):
        print("\nNo parameters provided. Using default values:")
        print(f"Addresses: {DEFAULT_ADDRESSES}")
        print(f"Start date: {DEFAULT_START_DATE}")
        print(f"End date: {DEFAULT_END_DATE}\n")
    
    # Use provided arguments or defaults
    addresses = args.addresses if args.addresses else DEFAULT_ADDRESSES
    start_date = args.start_date if args.start_date else DEFAULT_START_DATE
    end_date = args.end_date if args.end_date else DEFAULT_END_DATE
    
    print("Starting Dune Analytics data extraction...")
    
    # Execute query with parameters
    results_df = execute_dune_query(addresses, start_date, end_date)
    
    # Save to CSV
    write_to_csv(results_df)
    
    # Print first 10 rows
    print("\nFirst 10 rows of the results:")
    print(results_df.head(10))
    
    print("\nData extraction and CSV writing completed successfully.")

if __name__ == "__main__":
    main()
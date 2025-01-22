# dune
Dune analytics queries

## Setup and Usage (Linux)

### Prerequisites
- Python 3.8 or higher
- A Dune Analytics API key

### Installation

1. Clone the repository
```bash
git clone https://github.com/karolsudol/dune.git
cd dune/apps
```

2. Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install required packages
```bash
pip install -r requirements.txt
```

4. Set up environment variables
```bash
# Create .env file
echo "DUNE_API_KEY=your_api_key_here" > .env
```

### Running the Transaction Count Script

Basic usage:
```bash
python3 get_txs_cnt.py
```

With optional parameters:
```bash
python3 get_txs_cnt.py --addresses ADDRESS1 ADDRESS2 --start-date YYYY-MM-DD --end-date YYYY-MM-DD
```

Parameters:
- `--addresses`: One or more Ethereum addresses to analyze (space-separated)
- `--start-date`: Start date in YYYY-MM-DD format
- `--end-date`: End date in YYYY-MM-DD format

Default values:
- Addresses: 
  - 0x819f833BAe5deA66f0ABAb1E8723eBE105987e1C
  - 0xb7d1a295aad9e1816ec16c9835dc4373dadf646c
- Date range: Last 30 days

Example with parameters:
```bash
python3 get_txs_cnt.py --addresses 0x123... 0x456... --start-date 2024-01-01 --end-date 2024-03-01
```

The script will:
- Analyze transactions for the specified addresses
- Output results to `transaction_counts.csv`

Note: Make sure to replace `your_api_key_here` in the `.env` file with your actual Dune API key.
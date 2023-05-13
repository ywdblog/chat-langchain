# Bash script to ingest data
# This involves scraping the data from the web and then cleaning up and putting in Weaviate.
# Error if any command fails
set -e
git clone https://github.com/openai/openai-cookbook
python3 ingest_git.py

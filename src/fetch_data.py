import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Inisialisasi Kaggle API
api = KaggleApi()
api.authenticate()

# Download dataset ke direktori saat ini
dataset = 'khushipitroda/stock-market-historical-data-of-top-10-companies'
api.dataset_download_files(dataset, path='data/raw', unzip=True)

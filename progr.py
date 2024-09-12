from stock_data_fetcher import StockDataFetcher
from netflix_stock_dashboard import NetflixStockDashboard

# Fetch stock data
fetcher = StockDataFetcher("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html")
fetcher.run()

# If the data was successfully fetched and cleaned, initialize the dashboard
if not fetcher.data.empty:
    dashboard = NetflixStockDashboard(fetcher.data)
    dashboard.run()

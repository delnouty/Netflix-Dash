import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

class StockDataFetcher:
    def __init__(self, url, save_csv=True, plot_data=True):
        self.url = url
        self.data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"])
        self.save_csv = save_csv
        self.plot_data = plot_data

    def fetch_html(self):
        """Fetch the HTML content of the webpage."""
        try:
            print("Fetching HTML from:", self.url)
            response = requests.get(self.url)
            response.encoding = response.apparent_encoding
            if response.status_code == 200:
                print("HTML fetched successfully!")
                return response.text
            else:
                print(f"Failed to fetch HTML. Status code: {response.status_code}")
                return None
        except requests.RequestException as e:
            print("An error occurred while fetching the HTML:", e)
            return None

    def parse_html(self, html):
        """Parse HTML content to extract stock data."""
        try:
            soup = BeautifulSoup(html, 'html5lib')
            title = soup.find("h1").get_text(strip=True)
            print('Page title:', title)
            
            table_body = soup.find("tbody")
            if not table_body:
                raise ValueError("Table body not found in the HTML content")
            
            rows = table_body.find_all('tr')
            if not rows:
                raise ValueError("No rows found in the table body")
            
            data = [
                {
                    "Date": row.find_all("td")[0].text,
                    "Open": row.find_all("td")[1].text,
                    "High": row.find_all("td")[2].text,
                    "Low": row.find_all("td")[3].text,
                    "Close": row.find_all("td")[4].text,
                    "Adj Close": row.find_all("td")[5].text,
                    "Volume": row.find_all("td")[6].text.strip().replace(',', '')
                }
                for row in rows
            ]
            self.data = pd.DataFrame(data)
            print("Data parsing successful!")
        except Exception as e:
            print("Error while parsing HTML:", e)

    def clean_data(self):
        """Clean the stock data and convert to appropriate data types."""
        try:
            print("Cleaning and formatting data...")
            self.data["Date"] = pd.to_datetime(self.data["Date"], errors='coerce')
            self.data["Volume"] = pd.to_numeric(self.data["Volume"], errors='coerce')
            self.data[["Open", "High", "Low", "Close", "Adj Close"]] = self.data[["Open", "High", "Low", "Close", "Adj Close"]].apply(pd.to_numeric, errors='coerce')
            print("Data cleaning completed!")
        except Exception as e:
            print("Error while cleaning data:", e)

    def save_to_csv(self, filename='StockData.csv'):
        """Save the DataFrame to a CSV file."""
        try:
            if self.save_csv:
                print(f"Saving data to {filename}...")
                self.data.to_csv(filename, index=False)
                print(f"Data successfully saved to {filename}")
            else:
                print("Saving to CSV is disabled.")
        except Exception as e:
            print("Error while saving data to CSV:", e)

    def plot_stock_data(self):
        """Plot stock data using candlestick chart."""
        try:
            if self.plot_data:
                print("Plotting stock data...")
                self.data.set_index('Date', inplace=True)
                mpf.plot(self.data, type='candle', style='charles', title='Stock Price', ylabel='Price', volume=True)
                print("Plot generated successfully!")
            else:
                print("Plotting is disabled.")
        except Exception as e:
            print("Error while plotting data:", e)

    def run(self):
        """Main method to fetch, clean, save and plot data."""
        print("Starting data fetch process...")
        html = self.fetch_html()
        if html:
            self.parse_html(html)
            if not self.data.empty:
                self.clean_data()
                print(self.data.head())  # Display first few rows as a check
                print(self.data.dtypes)
                self.save_to_csv()
                self.plot_stock_data()
        print("Process completed!")

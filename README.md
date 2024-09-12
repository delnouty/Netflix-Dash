# Netflix-Dash
Web-Based Data Dashboard. 

- StockDataFetcher: This class is responsible for fetching, cleaning, and (optionally) saving and plotting the stock data.
- NetflixStockDashboard: This class will take the data fetched by StockDataFetcher and create a Dash dashboard to display the stock information in a table and candlestick chart.

## How It Works:
- StockDataFetcher Class:
  * Fetches stock data from the provided URL.
  * Parses, cleans, and optionally saves the data as CSV or plots it.
- NetflixStockDashboard Class:
    * Takes the cleaned stock data provided by StockDataFetcher and builds a Dash dashboard.
    * Displays a table of stock data and a candlestick chart using Plotly.
## Example Usage:
- First, the StockDataFetcher fetches and processes the stock data.
- Then, the NetflixStockDashboard uses the processed data to generate a dashboard.

## What is it?
The application is building using Dash. It is a combination of both front-end and back-end components, but Dash abstracts away much of the traditional separation between the two. Here’s how it breaks down:

1. Front-End (User Interface / Client-Side). It has a front-end: The interactive visualizations, graphs, tables, and buttons are all part of the front-end. These are the elements users see and interact with in a web browser. Dash uses HTML, CSS, and JavaScript under the hood to create the front-end. However, as a developer, you don't have to write these directly; Dash generates them for you using Python. Plotly (the graphing library Dash is built on) is responsible for rendering the interactive charts in the browser using JavaScript.
2. Back-End (Server-Side). The logic for fetching, processing, and preparing data (e.g., fetching stock data from a website, cleaning it, and generating the figures) happens on the back-end. Dash is built on Flask, which is a Python-based web framework. Flask runs the server, manages routes, and processes the data before it's sent to the front-end.
Python handles the back-end logic, interacting with libraries like requests for fetching data and pandas for data processing.

### What Does Dash Handle?
1. Front-End: HTML components (e.g., html.Div(), html.H1()) and interactive graphs (via dcc.Graph()).
2. Back-End: Data processing, generating the layout, and handling user input.
### Is Dash Front-End or Back-End?
Both: While it primarily works with Python in Dash, it handles both front-end (what the user sees) and back-end (data fetching and processing).
From a Developer’s Perspective: You’re building a full-stack web application without needing to separately manage front-end technologies like HTML, CSS, or JavaScript.
In short, Dash applications are considered full-stack applications, combining both front-end and back-end functionality in a seamless Python environment.

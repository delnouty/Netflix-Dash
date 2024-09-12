import dash
import dash_table
from dash import dcc
from dash import html
import plotly.graph_objects as go

class NetflixStockDashboard:
    def __init__(self, stock_data):
        """Initialize the dashboard with the provided stock data."""
        self.app = dash.Dash(__name__)
        self.stock_data = stock_data
        self.build_layout()

    def create_candlestick_chart(self):
        """Create a candlestick chart using Plotly."""
        fig = go.Figure(
            data=[
                go.Candlestick(
                    x=self.stock_data.index,
                    open=self.stock_data['Open'],
                    high=self.stock_data['High'],
                    low=self.stock_data['Low'],
                    close=self.stock_data['Close'],
                    increasing_line_color='green',
                    decreasing_line_color='red',
                    name='Stock'
                )
            ]
        )
        fig.update_layout(
            title='Stock Price',
            xaxis_title='Date',
            yaxis_title='Price',
            xaxis_rangeslider_visible=False
        )
        return fig

    def build_layout(self):
        """Build the Dash layout."""
        self.app.layout = html.Div([
            html.H1('Stock Price Dashboard'),

            # Table displaying stock data
            html.Div([
                dash_table.DataTable(
                    id='table',
                    columns=[{"name": i, "id": i} for i in self.stock_data.reset_index().columns],
                    data=self.stock_data.reset_index().to_dict('records'),
                    style_table={'height': '300px', 'overflowY': 'auto'},
                    page_size=10
                )
            ], style={'padding': '24px'}),

            # Candlestick chart
            html.Div([
                dcc.Graph(
                    id='candlestick-chart',
                    figure=self.create_candlestick_chart()
                )
            ])
        ])

    def run(self):
        """Run the Dash app."""
        self.app.run_server()

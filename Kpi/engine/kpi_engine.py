import pandas as pd

class KPIEngine:
    def __init__(self, df):
        self.df = df

    def compute_kpis(self):
        return {
            "Total Revenue": self.df['revenue'].sum(),
            "Avg Sessions": self.df['sessions'].mean(),
            "Conversion Rate": self.df['users'].sum() / self.df['sessions'].sum()
        }

    def growth_analysis(self):
        self.df['growth'] = self.df['revenue'].diff()
        return self.df[['date','growth']]

    def rolling_metrics(self, window=3):
        self.df['rolling_revenue'] = self.df['revenue'].rolling(window).mean()
        return self.df[['date','rolling_revenue']]

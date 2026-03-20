import pandas as pd
from config import Config
from engine.kpi_engine import KPIEngine
from utils.logger import get_logger
from viz.plots import plot_growth

def main():
    logger = get_logger()
    df = pd.read_csv(Config.DATA_PATH)

    engine = KPIEngine(df)

    logger.info("Computing KPIs")
    print(engine.compute_kpis())

    growth = engine.growth_analysis()
    plot_growth(growth)

if __name__ == "__main__":
    main()

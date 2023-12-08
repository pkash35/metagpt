## data_generator.py

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class DataGenerator:
    def __init__(self, years: int = 1):
        self.years = years

    def generate(self) -> pd.DataFrame:
        start_date = datetime.now() - timedelta(days=365 * self.years)
        dates = pd.date_range(start=start_date, end=datetime.now())
        sales = np.random.randint(1, 100, size=len(dates))

        data = pd.DataFrame({
            'date': dates,
            'sales': sales
        })

        return data

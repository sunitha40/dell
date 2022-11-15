import numpy as np
import pandas as pd

df = pd.read_csv("https://www.fruityvice.com/api/fruit/watermelon")
streamlit.dataframe(df)

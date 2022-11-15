import streamlit

import numpy as np
import pandas as pd
streamlit.text("hello")
df = pd.read_csv("https://www.fruityvice.com/api/fruit/watermelon")
streamlit.dataframe(df)

import streamlit

import numpy as np
import pandas as pd
streamlit.text("hello")
df = pd.read_csv("abc.txt")
streamlit.dataframe(df)

import pandas as pd
import numpy as np

var = pd.read_csv("C:/Users/user/OneDrive/Desktop/Fods/StudentData1.csv")
varhead=var.head()
print("mean of maths scores dataset is",np.mean(varhead.Maths))
print("mean of Science scores dataset is",np.mean(varhead.Science))
print("mean of English scores dataset is",np.mean(varhead.English))
print("mean of history scores dataset is",np.mean(varhead.History))

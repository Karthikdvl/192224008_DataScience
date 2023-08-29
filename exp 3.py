import pandas as pd
import numpy as np

hd=pd.read_csv("C:/Users/user/OneDrive/Desktop/Fods/Housedata.csv")
t=hd[hd.NoOfBedrooms>4]
t1=np.mean(t.SalesPriceInLakhs)
print(t1)

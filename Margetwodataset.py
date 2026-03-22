import pandas as pd
df1 = pd.DataFrame({'id':[1,2,3],'sales':[100,200,300]})
df2 = pd.DataFrame({'id':[1,2,3],'promo':[True,False,True]})
merged = pd.merge(df1, df2, on='id')
print(merged[merged['promo']==True]['sales'].sum())
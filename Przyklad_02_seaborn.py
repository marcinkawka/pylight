import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
#przygotowanie danych
df =pd.read_csv('dane_zsumowane_z_pogoda.csv')
df['dzien']=pd.to_datetime(df['Data'])
df.set_index(['dzien'],inplace=True)
df_pogoda = df[['temp_max','temp_min']]
df_2016 = df[df.index.year==2016]
df_2017 = df[df.index.year==2017]
df_2018 = df[df.index.year==2018]
#
most_gdanski = 'NSR Most Gdański DDR'
solec = 'NSR Solec DDR'
# Show each distribution with both violins and points
#brzydkie
#sns.violinplot(data=df[most_gdanski][df.index.year==2017],  inner="points")
#sns.violinplot(data=df[['temp_max','temp_min']])
#sns.lineplot(y=most_gdanski,x=df_2017.index, data=df_2017)

dd=df_2017.groupby(pd.Grouper(freq="M")).agg(['max']) 
dd.fillna(0,inplace=True)
del dd['Data']
del dd['startTyg']                                                                                                                                                                                                 
del dd['startM'] 
del dd['Jaki_dzien']
del dd['Rodzaj_opadu']

sns.heatmap(dd.T,annot=True)
plt.show()



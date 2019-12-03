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

dd=df_2017.groupby(pd.Grouper(freq="M")).agg(['max']) 
dd.fillna(0,inplace=True)

# kasowanie nieinteresujących kolumn
dd.drop(['temp_min','temp_max','temp_avg','deszcz'],axis=1,inplace=True)
dd.drop(['Lp','Data','startTyg','startM','Jaki_dzien','Rodzaj_opadu'],axis=1,inplace=True)
#rzutowanie na inty
dd=dd.astype(int)
ddT=dd.T
dd_posortowane = ddT.sort_values(by='2017-01-31',ascending=False)
#
most_gdanski = 'NSR Most Gdański DDR'
solec = 'NSR Solec DDR'
# Show each distribution with both violins and points
#brzydkie
#sns.violinplot(data=df[most_gdanski][df.index.year==2017],  inner="points")
#sns.violinplot(data=df[['temp_max','temp_min']])
#sns.lineplot(y=most_gdanski,x=df_2017.index, data=df_2017)


#ax = sns.heatmap(dd_posortowane)
# trochę ładniej
ax = sns.heatmap(dd_posortowane,annot=True,fmt="5",annot_kws={"size": 10},cmap='jet')

# opis osi w miesiącach
ax.set_xticklabels(dd_posortowane.columns.strftime('%B'),rotation=0 )

# pokaż wykres
plt.show()



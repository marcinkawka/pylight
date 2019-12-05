import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import cartopy.crs as ccrs
from cartopy.io.img_tiles import Stamen

import colorsys
#przygotowanie danych
df = pd.read_csv('dane_zsumowane_z_pogoda.csv')
df_lokalizacja=pd.read_csv("polozenie_licznikow.csv") 
df['dzien']=pd.to_datetime(df['Data'])

#ustawianie indexów
df.set_index(['dzien'],inplace=True)
df_lokalizacja.set_index(['Miejsce'],inplace=True) 

#obliczamy maksimum roczne
df_2017 = df[df.index.year==2017]
df_max_2017 = df_2017.groupby(pd.Grouper(freq="Y")).agg('max')


df_calosc = pd.concat([df_lokalizacja,df_max_2017.T],axis=1,sort=True).dropna()
df_calosc.columns  = ['id','lat','lon','max_roczne']

#Rodzaj mapy z serwisu maps.stamen.com: Toner, Terrain
#Smak (flavour) mapy: lite, bakgroudm, labels
kafelki_podkładowe = Stamen('toner-lite')
#kafelki_podkładowe = Stamen('terrain')
uklad_wspolrzednych = kafelki_podkładowe.crs

# Odwzorowanie walcowe równoodległościowe
projekcjaKartograficzna = ccrs.PlateCarree()

# Tworzenie rysunku Matplotlib, wymiary w calach
fig = plt.figure(figsize=(10,10),dpi=50)

#dodajemy osie z prawej strony i u góry
ax = fig.add_axes([0, 0, 1, 1], projection=kafelki_podkładowe.crs)

#ustawiamy zakres -> kolejność argumentów  (x_min, x_max, y_min, y_max) 
ax.set_extent([20.8, 21.13, 52.15, 52.3], crs=projekcjaKartograficzna)

totalne_maksimum = df_calosc['max_roczne'].max()

cmap = mpl.cm.Blues
#DODAĆ LEGENDĘ!!!
for licznik in df_calosc.iterrows():
	lat = licznik[1]['lat']
	lon = licznik[1]['lon']
	rozmiar_znacznika = 5+round(30*licznik[1]['max_roczne']/totalne_maksimum)
	kolor_rgb = colorsys.hsv_to_rgb(licznik[1]['max_roczne']/totalne_maksimum,0.8,0.8)

	ax.plot(lon,lat,linestyle='',\
		markersize=rozmiar_znacznika,\
		marker='o', color=kolor_rgb,transform=projekcjaKartograficzna)



#dodać zmianę koloru/rozmiaru w zależności od natężenia ruchu
#df.groupby(df.index.year).agg(['sum','mean','max'])  

#dodajemy mapę podkładową
#poziom szczegółowości 1-globalny, 14- poziom ulicy
ax.add_image(kafelki_podkładowe, 13)
plt.grid(True)
plt.show()

#plt.savefig('Nasza_mapka.png')


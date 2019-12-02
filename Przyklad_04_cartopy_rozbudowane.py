import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.io.img_tiles import Stamen


#przygotowanie danych
df =pd.read_csv('dane_zsumowane_z_pogoda.csv')
df['dzien']=pd.to_datetime(df['Data'])
df.set_index(['dzien'],inplace=True)


df_lokalizacja=pd.read_csv("polozenie_licznikow.csv") 


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

#dodajemy do mapy punkt o współrzędnych (20.9,52.2)
for licznik in df_lokalizacja[['Miejsce','lat','lon']].iterrows():
    lat = licznik[1]['lat']
    lon = licznik[1]['lon']
    nazwa_licznika = licznik[1]['Miejsce']

#dodać zmianę koloru/rozmiaru w zależności od natężenia ruchu
#df.groupby(df.index.year).agg(['sum','mean','max'])  
    ax.plot(lon,lat,linestyle='',markersize=9,\
        marker='o', color='blue',transform=projekcjaKartograficzna)

#dodajemy mapę podkładową
#poziom szczegółowości 1-globalny, 14- poziom ulicy
ax.add_image(kafelki_podkładowe, 13)
plt.grid(True)
plt.show()


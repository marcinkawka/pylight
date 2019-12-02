import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.io.img_tiles import Stamen

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
ax.plot(20.9,52.2,linestyle='',markersize=9,\
    marker='o', color='blue',transform=projekcjaKartograficzna)

#dodajemy mapę podkładową
#poziom szczegółowości 1-globalny, 14- poziom ulicy
ax.add_image(kafelki_podkładowe, 13)
plt.grid(True)
plt.show()


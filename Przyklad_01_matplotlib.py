import matplotlib.pyplot as plt
import pandas as pd 

# wczytywanie danych z csv za pomocą pandas
df=pd.read_csv('tasmax_count_gt_30_rcp45_Warszawa_trend.csv')
#wybór zmiennej do wykresu
y = df['liczba_dni']

#proste rysowanie wykresu
#plt.plot(y)
#plt.show()

#dodajmy zmienną niezależną
x=range(2007,2093)
plt.plot(x,y,'kx')
#i kilka ozdobników
plt.grid(True)
plt.xlabel('Rok')
plt.ylabel('Liczba dni w roku')
plt.title('Liczba dni w roku z temperaturą maksymalną powyżej 30 stopni')

plt.show()


#subploty

# Zapis do pliku zamiast na ekran
#plt.savefig('foo.pdf')
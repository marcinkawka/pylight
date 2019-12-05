import matplotlib.pyplot as plt
import pandas as pd 

# wczytywanie danych z csv za pomocą pandas
df = pd.read_csv('dane_zsumowane_z_pogoda.csv')
df['dzien']=pd.to_datetime(df['Data'])
df.set_index(['dzien'],inplace=True)
#wybór zmiennej do wykresu
kolumna1 = 'Marszałkowska/Metro Świętokrzyska'
kolumna2 = 'Banacha/Żwirki i Wigury'
kolumna3 = 'Belwederska'
'''
#proste rysowanie wykresu
plt.plot(df[[kolumna1,kolumna2]])

#kilka ozdobników
plt.legend([kolumna1,kolumna2])
plt.title('Dzienna liczba rowerzystów')
plt.grid(True)
plt.show()

'''
#wykres rozproszenia
#plt.scatter(x=df[kolumna1],y=df[kolumna2])
#plt.show()

'''
#subploty (3,1, przełącz na 1), notacja Matlabowa
plt.subplot(3,1,1)
plt.plot(df[kolumna1])
plt.subplot(3,1,2)
plt.plot(df[kolumna2])
plt.subplot(3,1,3)
plt.plot(df[kolumna3])
plt.show()

#To samo, ale bardziej elegancko, notacja Pythonowa
fig1, ax = plt.subplots(3,1,sharex=True)
l1, = ax[0].plot(df[kolumna1],color='r')
l2, = ax[1].plot(df[kolumna2],color='g')
l3, = ax[2].plot(df[kolumna3],color='b')
plt.legend([l1,l2,l3],[kolumna1,kolumna2,kolumna3])
plt.grid(True)
plt.show()
'''
# Zapis do pliku zamiast na ekran
#plt.savefig('foo.pdf')
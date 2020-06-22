import pandas as pd
import matplotlib.pyplot as plt

## BU KODDA SABİHA GÖKÇEN VE ATATRÜK HAVAALANLARININ 2018 YILINA KADAR OLAN VERİLERİ VE 2018 YILINDAN SONRA
## TAHMİNLERLE YOLA ÇIKILARAK BULUNMUŞ KAPASİTE SAYILARI KARŞILAŞTIRILMIŞTIR

df = pd.read_csv('veriler.csv')
print(df)

ucusAtaturk = df.loc[:,'Atatürk']
kapasiteAtaturk = df.loc[:, 'AtatürkKapasite']
tarihlerAtaturk = df.loc[:, 'Tarih']

diziAtaturk = []
sayac = 0
for i in range(len(df)):
    if ucusAtaturk[i] - kapasiteAtaturk[i]>0:
        diziAtaturk.append(tarihlerAtaturk[i])
        i = i + 1
print('Atatürk Havalimanında Kapasite Aşılan Aylar(2019 Yılı Sonrası Tahmin edilerek yazılmıştır)')
print(diziAtaturk)
print('Atatürk Havalimanında Kapasite Aşılan Aylar Toplamı:' , len(diziAtaturk))

ucusSabiha = df.loc[:,'SabihaGökçen']
kapasiteSabiha = df.loc[:, 'SabihaKapasite']
tarihlerSabiha = df.loc[:, 'Tarih']

diziSabiha = []
sayac = 0
for i in range(len(df)):
    if ucusSabiha[i] - kapasiteSabiha[i]>0:
        diziSabiha.append(tarihlerSabiha[i])
        i = i + 1
print('Sabiha Gökçen Havalimanında Kapasite Aşılan Aylar(2019 Yılı Sonrası Tahmin edilerek yazılmıştır)')
print(diziSabiha)
print('Sabiha Gökçen Havalimanında Kapasite Aşılan Aylar Toplamı:' , len(diziSabiha))

plt.figure(figsize=(12,10))
plt.subplot(2,2,1)  
plt.title("Atatürk Havaalanı Kapasitesi Karşılaştırılması")
plt.plot(df.Tarih,df.Atatürk,color="blue")
plt.plot(df.AtatürkKapasite,color="red")
plt.xlabel("Tarih")
plt.ylabel("Yolcu Sayıları")

plt.subplot(2,2,2)
plt.title("Sabiha Gökçen Havaalanı Kapasitesi Karşılaştırılması")
plt.plot(df.Tarih,df.SabihaGökçen,color="blue")
plt.plot(df.SabihaKapasite,color="red")
plt.xlabel("Tarih")
plt.ylabel("Yolcu Sayıları")

plt.show()







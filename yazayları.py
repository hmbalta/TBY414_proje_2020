import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('yazayları.csv')
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
print('Atatürk Havalimanında Kapasite Aşılan Yaz Ayları(2019 Yılı Sonrası Tahmin edilerek yazılmıştır)')
print(diziAtaturk)
print('Atatürk Havalimanında Kapasite Aşılan Yaz Ayları Toplamı:' , len(diziAtaturk))

ucusSabiha = df.loc[:,'Sabiha']
kapasiteSabiha = df.loc[:, 'SabihaKapasite']
tarihlerSabiha = df.loc[:, 'Tarih']

diziSabiha = []
sayac = 0
for i in range(len(df)):
    if ucusSabiha[i] - kapasiteSabiha[i]>0:
        diziSabiha.append(tarihlerSabiha[i])
        i = i + 1
print('Sabiha Gökçen Havalimanında Kapasite Aşılan Yaz Ayları(2019 Yılı Sonrası Tahmin edilerek yazılmıştır)')
print(diziSabiha)
print('Sabiha Gökçen Havalimanında Kapasite Aşılan Yaz Ayları Toplamı:' , len(diziSabiha))

plt.figure(figsize=(12,10))
plt.subplot(2,2,1)  
plt.title("Atatürk Havaalanı Kapasitesi Yaz Aylarının Karşılaştırılması")
plt.plot(df.Tarih,df.Atatürk,color="blue")
plt.plot(df.AtatürkKapasite,color="red")
plt.xlabel("Tarih")
plt.ylabel("Yolcu Sayıları")

plt.subplot(2,2,2)
plt.title("Sabiha Gökçen Havaalanı Kapasitesi Yaz Aylarının Karşılaştırılması")
plt.plot(df.Tarih,df.Sabiha,color="blue")
plt.plot(df.SabihaKapasite,color="red")
plt.xlabel("Tarih")
plt.ylabel("Yolcu Sayıları")

plt.show()







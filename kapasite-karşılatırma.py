import pandas as pd

df = pd.read_csv('veriler.csv')
print(df)

ucusAtaturk = df.loc[:,'Atatürk']
kapasiteAtaturk = df.loc[:, 'Atatürk Kapasite']
tarihlerAtaturk = df.loc[:, 'Unnamed: 0']

diziAtaturk = []
sayac = 0
for i in range(len(df)):
    if ucusAtaturk[i] - kapasiteAtaturk[i]>0:
        diziAtaturk.append(tarihlerAtaturk[i])
        i = i + 1
print('Atatürk Havalimanında Kapasite Aşılan Aylar')
print(diziAtaturk)
print('Atatürk Havalimanında Kapasite Aşılan Aylar Toplamı:' , len(diziAtaturk))

ucusSabiha = df.loc[:,'Sabiha Gökçen']
kapasiteSabiha = df.loc[:, 'Sabiha Kapasite']
tarihlerSabiha = df.loc[:, 'Unnamed: 0']

diziSabiha = []
sayac = 0
for i in range(len(df)):
    if ucusSabiha[i] - kapasiteSabiha[i]>0:
        diziSabiha.append(tarihlerSabiha[i])
        i = i + 1
print('Sabiha Gökçen Havalimanında Kapasite Aşılan Aylar')
print(diziAtaturk)
print('Sabiha Gökçen Havalimanında Kapasite Aşılan Aylar Toplamı:' , len(diziSabiha))



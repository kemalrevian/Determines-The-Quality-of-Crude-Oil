import pandas as pd
import numpy as np

def SG(dft,dfs):
    SG = dft/dfs
    return SG
def API(SG):
    API = (141.5/SG)-131.5
    return API
def klasSG_API():
    data = {
    "Kualitas":["Ringan", "Medium Ringan", "Medium Berat" , "Berat", "Sangat Berat"],
    "Spesific Gravity" :["< 0.830","0.830 - 0.850","0.850 - 0.865","0.865 - 0.905","> 0.905"],
    "API":['> 39.0','39.0 - 35.0','35.0 - 32.1','32.1 - 24.0','< 24.8']
    }
    df = pd.DataFrame(data)
    print(df)
while True:
    print("SELAMAT DATANG DI PROGRAM \nPENENTUAN KUALITAS MINYAK BUMI" )
    print("<<<<<MENU>>>>>")
    print(" [A] Klasifikasi SG dan API\n [B] Perhitungan SG dan API\n [X] Exit ")
    print("==============")
    option = input("Pilih Menu Anda:")
    if option == "A":
        print("=====TABEL KLASIFIKASI MINYAK BUMI MENURUT SG DAN API=====")
        print(klasSG_API())
    elif option == "B":
        print("=====PERHITUNGAN SG dan API=====")
        dft= float(input("masukkan nilai Densitas Fluida Terhitung : "))
        dfs= float(input("masukkan nilai Densitas Fluida Standar : "))
        print("Nilai SG :", SG(dft,dfs))
        print("Nilai API :",API(SG(dft,dfs)))
        SG_0 = float(SG(dft,dfs))
        API_0 = float(API(SG(dft,dfs)))
        while True:
            if SG_0 < 0.830 and API_0 > 39.0:
                print("Kualitas Minyak Bumi : Ringan")
                break 
            elif 0.850 > SG_0 >= 0.830 and 35.0 < API_0 <= 39.0:
                print ("Kualitas Minyak Bumi : Medium Ringan")
                break
            elif 0.865 > SG_0 >= 0.850 and 32.1 < API_0 <= 35.0:
                print ("Kualitas Minyak Bumi : Medium Berat")
                break
            elif 0.905 > SG_0 >= 0.865 and 24.0 < API_0 <= 32.1:
                print ("Kualitas Minyak Bumi : Berat")
                break
            elif SG_0 > 0.905 and API_0 < 24.8:
                print ("Kualitas Minyak Bumi : Sangat Berat")
                break
    elif option == "X":
        print("TERIMA KASIH")
        break    
    else:
        print("!!! HARAP MASUKKAN KODE YANG BENAR !!!")
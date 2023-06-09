# Masukkan library dan fungsi yang dibutuhkan
import pandas
from datetime import datetime

# Ambil dataset dan hitung losses data
def SubsistemIdentifikasiLossesDataAIS(TipeKapal, NamaExcel):
    # Membuat program dapat membaca isi excel yang diinput melalui NamaExcel
    DataIsiExcel = pandas.read_csv(NamaExcel)
    # Data isi excel yang berbaris2 dan berkolom2 dinamakan variabel DataPerjalananKapal dengan menggunakan DataIsiExcel.values
    DataPerjalananKapal = DataIsiExcel.values

    
    for i in range(len(DataPerjalananKapal)-1):
        timenow_hari=DataPerjalananKapal[i][1].replace("/",":")
        timenow_gabungan = f"{timenow_hari}:{DataPerjalananKapal[i][2]}"
        timenow = datetime.strptime(timenow_gabungan, "%d:%m:%Y:%H:%M")

        timenext_hari=DataPerjalananKapal[i+1][1].replace("/",":")
        timenext_gabungan = f"{timenext_hari}:{DataPerjalananKapal[i+1][2]}"
        timenext = datetime.strptime(timenext_gabungan, "%d:%m:%Y:%H:%M")

        deltatime = timenext - timenow

        
        if int(deltatime.total_seconds()) >= 7200:
            print(f'Ya, kapal {TipeKapal} terjadi losses data AIS selama: {int(deltatime.total_seconds())} detik dan terindikasi melakukan IUU transshipment')
            losses_data = True
        elif 360 < deltatime.total_seconds() < 7200:
            print(f'Ya, kapal {TipeKapal} terjadi losses data AIS selama: {int(deltatime.total_seconds())} detik tetapi tidak terindikasi melakukan IUU transshipment')
            losses_data = True
        else:
            print(f'Kapal {TipeKapal} tidak terjadi losses data AIS dan tidak terindikasi melakukan IUU transshipment')
            losses_data = False
    if losses_data :
        print(f'Kesimpulan : Pada kapal {TipeKapal} ditemukan bahwa telah terjadi losses data AIS')
    elif losses_data == False :
        print(f'Kesimpulan : Pada kapal {TipeKapal} ditemukan bahwa tidak terjadi losses data AIS')

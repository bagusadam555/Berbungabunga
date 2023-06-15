# Masukkan library dan fungsi yang dibutuhkan
import pandas
from datetime import datetime

# Ambil dataset dan hitung losses data
def SubsistemIdentifikasiLossesDataAIS(TipeKapal, NamaExcel):
    # Membuat program dapat membaca isi excel yang diinput melalui NamaExcel
    DataIsiExcel = pandas.read_csv(NamaExcel)
    # Data isi excel yang berbaris2 dan berkolom2 dinamakan variabel DataPerjalananKapal dengan menggunakan DataIsiExcel.values
    DataPerjalananKapal = DataIsiExcel.values

    # Kondisi awal variabel losses_data dan variabel total_losses_data dalam program
    losses_data = False  
    total_losses_data = 0  

    # Mengatur cara kerja perhitungan selisih waktu
    for i in range(len(DataPerjalananKapal)-1):
        timenow_hari = DataPerjalananKapal[i][1].replace("/", ":")
        timenow_gabungan = f"{timenow_hari}:{DataPerjalananKapal[i][2]}"
        timenow = datetime.strptime(timenow_gabungan, "%d:%m:%Y:%H:%M")

        timenext_hari = DataPerjalananKapal[i+1][1].replace("/", ":")
        timenext_gabungan = f"{timenext_hari}:{DataPerjalananKapal[i+1][2]}"
        timenext = datetime.strptime(timenext_gabungan, "%d:%m:%Y:%H:%M")

        deltatime = timenext - timenow

        if int(deltatime.total_seconds()) >= 7200:
            print(f'Ya, kapal {TipeKapal} terjadi losses data AIS selama: {deltatime} dan terindikasi melakukan IUU transshipment')
            #kondisi losses_data = true, maka total losses_data ditambahkan ke kondisi awal tadi
            losses_data = True
            total_losses_data += int(deltatime.total_seconds())
        elif 360 < deltatime.total_seconds() < 7200:
            print(f'Ya, kapal {TipeKapal} terjadi losses data AIS selama: {deltatime} tetapi tidak terindikasi melakukan IUU transshipment')
            #kondisi losses_data = true, maka total losses_data ditambahkan ke kondisi awal tadi
            losses_data = True
            total_losses_data += int(deltatime.total_seconds())
        else:
            print(f'Kapal {TipeKapal} tidak terjadi losses data AIS dan tidak terindikasi melakukan IUU transshipment')


    # Membuat kesimpulan
    if losses_data:
        hours = total_losses_data // 3600
        minutes = (total_losses_data % 3600) // 60
        seconds = total_losses_data % 60
        print(f'Kesimpulan: Pada kapal {TipeKapal} ditemukan bahwa telah terjadi losses data AIS selama: {hours} jam, {minutes} menit, {seconds} detik')
    else:
        print(f'Kesimpulan: Pada kapal {TipeKapal} tidak ditemukan adanya losses data AIS')

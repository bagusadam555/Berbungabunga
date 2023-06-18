from pyit2fls import Mamdani, rtri_mf,ltri_mf,IT2FS, IT2FLS, trapezoid_mf, tri_mf, IT2FS_plot, min_t_norm, max_s_norm, TR_plot, crisp
from numpy import linspace, meshgrid, zeros
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import pandas
#Defining an interval type 2 fuzzy set with trapzeoidal mf


#Jarak membership function
domainJarak= linspace(0,700, 7000)
Dekat = IT2FS(domainJarak,
 trapezoid_mf, [0, 2,   16,   18, 1.],
 trapezoid_mf, [1, 5, 12, 17, 0.5])
Jauh = IT2FS(domainJarak,
 trapezoid_mf, [17.3, 18, 685,700, 1.],
 trapezoid_mf, [18, 28, 680, 690, 0.5])
IT2FS_plot(Dekat, Jauh, legends=["Dekat", "Jauh"], filename="Jarak")

#BedaHeading membership function
domainBedaHeading = linspace(-6, 186, 19200)
OT = IT2FS(domainBedaHeading,
 trapezoid_mf, [-6, -5.8, 5.8, 6, 1.],
 trapezoid_mf, [-5.8, -4, 3, 5.8, 0.75]) 
C = IT2FS(domainBedaHeading,
 trapezoid_mf, [6, 10, 173,174,1.],
 trapezoid_mf, [8, 10, 170, 171,0.75]) 
HO = IT2FS(domainBedaHeading,
 trapezoid_mf, [174,175,185,186, 1.],
 trapezoid_mf, [174.5, 175, 180, 185, 0.75])
IT2FS_plot(OT, C, HO, legends=["OT", "C", "HO"], filename="BedaHeading")

#BedaKecepatan membership function
domainBedaKecepatan= linspace(-1., 20, 2000)
Kecil = IT2FS(domainBedaKecepatan,
 trapezoid_mf, [-0.1,   0,   3.3,   3.5, 1.],
 trapezoid_mf, [0.01, 0.5,     3,   3.5, 0.5])
Besar = IT2FS(domainBedaKecepatan,
 trapezoid_mf, [2.5, 3.6, 18, 20, 1.],
 trapezoid_mf, [2.6, 5, 15, 20, 0.5])
IT2FS_plot(Kecil, Besar, legends=["Kecil", "Besar"], filename="BedaKecepatan")

#KecepatanAngin membership function
domainKecepatanAngin= linspace(0., 27, 2700)
LowRisk =IT2FS(domainKecepatanAngin,
 trapezoid_mf, [0,     1,   14, 15.55,  1],
 trapezoid_mf, [0.5,   4,   10,  15.3, 0.75])
HighRisk = IT2FS(domainKecepatanAngin,
 trapezoid_mf, [13.61,   15.8,   26,    27,  1],
 trapezoid_mf, [13.77,     18,   23,  26.8, 0.75])
IT2FS_plot(LowRisk, HighRisk, legends=["LowRisk", "HighRisk"], filename="KecepatanAngin")

#JarakPandang membership function
domainJarakPandang = linspace(0, 10, 100)
TJ = IT2FS(domainJarakPandang,
 trapezoid_mf, [0,    0.25, 0.75, 1, 1.],
 trapezoid_mf, [0.11,  0.4,  0.6, 0.89, 0.75]) 
J = IT2FS(domainJarakPandang,
 trapezoid_mf, [0.6,  1,   9.4, 10, 1.],
 trapezoid_mf, [0.65, 3,    7, 10, 0.75])
IT2FS_plot(TJ, J, legends=["TJ", "J"], filename="JarakPandang")

# output membership function
domainKeputusan=linspace(0,100,10000); 
NoTrans = IT2FS(domainKeputusan,
 tri_mf,[0, 0.01,49,  1],
 tri_mf,[0, 15.01,48,0.55])
YesTrans = IT2FS(domainKeputusan,
 tri_mf,[49.1,  99, 100,  1],
 tri_mf,[  50,  85,  99,0.55])
IT2FS_plot(NoTrans,YesTrans,legends=["NoTrans","YesTrans"],filename="HasilKeputusan")

# An Interval Type 2 Fuzzy Logic System is created. The variables and output 

# variables are defined. As it can be seen, the system has 5 input and 1 output 

myIT2FLS = IT2FLS()
myIT2FLS.add_input_variable("Jarak") 
myIT2FLS.add_input_variable("BedaHeading") 
myIT2FLS.add_input_variable("BedaKecepatan") 
myIT2FLS.add_input_variable("KecepatanAngin") 
myIT2FLS.add_input_variable("JarakPandang")
myIT2FLS.add_output_variable("HasilKeputusan")

# the fuzzy IF-THEN rules
# 1 
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", OT), ("BedaKecepatan", Kecil), ("KecepatanAngin", LowRisk), ("JarakPandang", J)], 
                  [("HasilKeputusan", YesTrans)])
# 2
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", OT), ("BedaKecepatan", Kecil), ("KecepatanAngin", LowRisk), ("JarakPandang", TJ)], 
                  [("HasilKeputusan", YesTrans)])
# 3
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", OT), ("BedaKecepatan", Kecil), ("KecepatanAngin", HighRisk), ("JarakPandang", J)], 
                  [("HasilKeputusan", NoTrans)])
# 4
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", OT), ("BedaKecepatan", Kecil), ("KecepatanAngin", HighRisk), ("JarakPandang", TJ)], 
                  [("HasilKeputusan", NoTrans)])
# 5
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", OT), ("BedaKecepatan", Besar), ("KecepatanAngin", LowRisk), ("JarakPandang", J)], 
                  [("HasilKeputusan", NoTrans)])
# 6
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", OT), ("BedaKecepatan", Besar), ("KecepatanAngin", LowRisk), ("JarakPandang", TJ)], 
                  [("HasilKeputusan", NoTrans)])
# 7
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", OT), ("BedaKecepatan", Besar), ("KecepatanAngin", HighRisk), ("JarakPandang", J)], 
                  [("HasilKeputusan", NoTrans)])
# 8
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", OT), ("BedaKecepatan", Besar), ("KecepatanAngin", HighRisk), ("JarakPandang", TJ)], 
                  [("HasilKeputusan", NoTrans)])
# 9
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", C), ("BedaKecepatan", Kecil), ("KecepatanAngin", LowRisk), ("JarakPandang", J)], 
                  [("HasilKeputusan", NoTrans)])
# 10
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", C), ("BedaKecepatan", Kecil), ("KecepatanAngin", LowRisk), ("JarakPandang", TJ)], 
                  [("HasilKeputusan", NoTrans)])
# 11
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", C), ("BedaKecepatan", Kecil), ("KecepatanAngin", HighRisk), ("JarakPandang", J)], 
                  [("HasilKeputusan", NoTrans)])
# 12
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", C), ("BedaKecepatan", Kecil), ("KecepatanAngin", HighRisk), ("JarakPandang", TJ)], 
                  [("HasilKeputusan", NoTrans)])
# 13
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", C), ("BedaKecepatan", Besar), ("KecepatanAngin", LowRisk), ("JarakPandang", J)], 
                  [("HasilKeputusan", NoTrans)])
# 14
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", C), ("BedaKecepatan", Besar), ("KecepatanAngin", LowRisk), ("JarakPandang", TJ)], 
                  [("HasilKeputusan", NoTrans)])
# 15
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", C), ("BedaKecepatan", Besar), ("KecepatanAngin", HighRisk), ("JarakPandang", J)], 
                  [("HasilKeputusan", NoTrans)])
# 16
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", C), ("BedaKecepatan", Besar), ("KecepatanAngin", HighRisk), ("JarakPandang", TJ)], 
                  [("HasilKeputusan", NoTrans)])
# 17
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", HO), ("BedaKecepatan", Kecil), ("KecepatanAngin", LowRisk), ("JarakPandang", J)], 
                  [("HasilKeputusan", YesTrans)])
# 18
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", HO), ("BedaKecepatan", Kecil), ("KecepatanAngin", LowRisk), ("JarakPandang", TJ)], 
                  [("HasilKeputusan", YesTrans)])
# 19
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", HO), ("BedaKecepatan", Kecil), ("KecepatanAngin", HighRisk), ("JarakPandang", J)], 
                  [("HasilKeputusan", NoTrans)])
# 20
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", HO), ("BedaKecepatan", Kecil), ("KecepatanAngin", HighRisk), ("JarakPandang", TJ)], 
                  [("HasilKeputusan", NoTrans)])
# 21
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", HO), ("BedaKecepatan", Besar), ("KecepatanAngin", LowRisk), ("JarakPandang", J)], 
                  [("HasilKeputusan", NoTrans)])
# 22
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", HO), ("BedaKecepatan", Besar), ("KecepatanAngin", LowRisk), ("JarakPandang", TJ)], 
                  [("HasilKeputusan", NoTrans)])
# 23
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", HO), ("BedaKecepatan", Besar), ("KecepatanAngin", HighRisk), ("JarakPandang", J)], 
                  [("HasilKeputusan", NoTrans)])
# 24
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", HO), ("BedaKecepatan", Besar), ("KecepatanAngin", HighRisk), ("JarakPandang", TJ)], 
                  [("HasilKeputusan", NoTrans)])
# 25
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", OT), ("BedaKecepatan", Kecil), ("KecepatanAngin", LowRisk), ("JarakPandang", J)], 
                  [("HasilKeputusan", NoTrans)])
# 26
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", OT), ("BedaKecepatan", Kecil), ("KecepatanAngin", LowRisk), ("JarakPandang", TJ)], 
                  [("HasilKeputusan", NoTrans)])
# 27
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", OT), ("BedaKecepatan", Kecil), ("KecepatanAngin", HighRisk), ("JarakPandang", J)], 
                  [("HasilKeputusan", NoTrans)])
# 28
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", OT), ("BedaKecepatan", Kecil), ("KecepatanAngin", HighRisk), ("JarakPandang", TJ)], 
                  [("HasilKeputusan", NoTrans)])
# 29
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", OT), ("BedaKecepatan", Besar), ("KecepatanAngin", LowRisk), ("JarakPandang", J)], 
                  [("HasilKeputusan", NoTrans)])
# 30
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", OT), ("BedaKecepatan", Besar), ("KecepatanAngin", LowRisk), ("JarakPandang", TJ)], 
                  [("HasilKeputusan", NoTrans)])
# 31
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", OT), ("BedaKecepatan", Besar), ("KecepatanAngin", HighRisk), ("JarakPandang", J)], 
                  [("HasilKeputusan", NoTrans)])
# 32
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", OT), ("BedaKecepatan", Besar), ("KecepatanAngin", HighRisk), ("JarakPandang", TJ)], 
                  [("HasilKeputusan", NoTrans)])
# 33
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", C), ("BedaKecepatan", Kecil), ("KecepatanAngin", LowRisk), ("JarakPandang", J)], 
                  [("HasilKeputusan", NoTrans)])
# 34
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", C), ("BedaKecepatan", Kecil), ("KecepatanAngin", LowRisk), ("JarakPandang", TJ)], 
                  [("HasilKeputusan", NoTrans)])
# 35
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", C), ("BedaKecepatan", Kecil), ("KecepatanAngin", HighRisk), ("JarakPandang", J)], 
                  [("HasilKeputusan", NoTrans)])
# 36
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", C), ("BedaKecepatan", Kecil), ("KecepatanAngin", HighRisk), ("JarakPandang", TJ)], 
                  [("HasilKeputusan", NoTrans)])
# 37
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", C), ("BedaKecepatan", Besar), ("KecepatanAngin", LowRisk), ("JarakPandang", J)], 
                  [("HasilKeputusan", NoTrans)])
# 38
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", C), ("BedaKecepatan", Besar), ("KecepatanAngin", LowRisk), ("JarakPandang", TJ)], 
                  [("HasilKeputusan", NoTrans)])
# 39
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", C), ("BedaKecepatan", Besar), ("KecepatanAngin", HighRisk), ("JarakPandang", J)], 
                  [("HasilKeputusan", NoTrans)])
# 40
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", C), ("BedaKecepatan", Besar), ("KecepatanAngin", HighRisk), ("JarakPandang", TJ)], 
                  [("HasilKeputusan", NoTrans)])
# 41
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", HO), ("BedaKecepatan", Kecil), ("KecepatanAngin", LowRisk), ("JarakPandang", J)], 
                  [("HasilKeputusan", NoTrans)])
# 42
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", HO), ("BedaKecepatan", Kecil), ("KecepatanAngin", LowRisk), ("JarakPandang", TJ)], 
                  [("HasilKeputusan", NoTrans)])
# 43
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", HO), ("BedaKecepatan", Kecil), ("KecepatanAngin", HighRisk), ("JarakPandang", J)], 
                  [("HasilKeputusan", NoTrans)])
# 44
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", HO), ("BedaKecepatan", Kecil), ("KecepatanAngin", HighRisk), ("JarakPandang", TJ)], 
                  [("HasilKeputusan", NoTrans)])
# 45
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", HO), ("BedaKecepatan", Besar), ("KecepatanAngin", LowRisk), ("JarakPandang", J)], 
                  [("HasilKeputusan", NoTrans)])
# 46
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", HO), ("BedaKecepatan", Besar), ("KecepatanAngin", LowRisk), ("JarakPandang", TJ)], 
                  [("HasilKeputusan", NoTrans)])
# 47
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", HO), ("BedaKecepatan", Besar), ("KecepatanAngin", HighRisk), ("JarakPandang", J)], 
                  [("HasilKeputusan", NoTrans)])
# 48
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", HO), ("BedaKecepatan", Besar), ("KecepatanAngin", HighRisk), ("JarakPandang", TJ)], 
                  [("HasilKeputusan", NoTrans)])


def hasilidentifikasiiuu(NamaExcel):
    # Membuat program dapat membaca isi excel yang diinput melalui NamaExcel
    DataIsiExcel = pandas.read_csv(NamaExcel)
    # Data isi excel yang berbaris2 dan berkolom2 dinamakan variabel DataPerjalananKapal dengan menggunakan DataIsiExcel.values
    DataPerjalananKapal = DataIsiExcel.values

    # Mengatur cara kerja perhitungan selisih waktu
    for i in range(len(DataPerjalananKapal)-1):
        jarak = DataPerjalananKapal[i][3]
        BedaHeading = DataPerjalananKapal[i][4]
        BedaKecepatan = DataPerjalananKapal[i][5]
        KecepatanAngin = DataPerjalananKapal[i][6]
        JarakPandang = DataPerjalananKapal[i][7]
        it2out, tr=myIT2FLS.evaluate({"Jarak":jarak, "BedaHeading":BedaHeading,
                                       "BedaKecepatan":BedaKecepatan,
                                       "KecepatanAngin":KecepatanAngin,
                                       "JarakPandang":JarakPandang}, min_t_norm,max_s_norm,
                                       domainKeputusan,method="Centroid", algorithm="KM")
        #it2out["HasilKeputusan"].plot(filename="hasil Identifikasi IUU")
        #TR_plot(domainKeputusan, tr["HasilKeputusan"], filename="hasil Identifikasi IUU")
        hasil = ((crisp(tr["HasilKeputusan"])))
        print(hasil)
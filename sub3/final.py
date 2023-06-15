from pyit2fls import Mamdani, rtri_mf,ltri_mf,IT2FS, IT2FLS, trapezoid_mf, tri_mf, IT2FS_plot, min_t_norm, max_s_norm, TR_plot, crisp
from numpy import linspace, meshgrid, zeros
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

#Defining an interval type 2 fuzzy set with trapzeoidal mf


#Jarak membership function
domainJarak= linspace(0., 2000, 6000)
Dekat = IT2FS(domainJarak,
 trapezoid_mf, [0, 200,   780,   850, 1.],
 trapezoid_mf, [1, 250, 750, 830, 0.1])
Jauh = IT2FS(domainJarak,
 trapezoid_mf, [800, 1100, 1850,2000, 1.],
 trapezoid_mf, [850, 1100, 1800, 1950, 0.1])
IT2FS_plot(Dekat, Jauh, legends=["Dekat", "Jauh"], filename="Jarak")

#BedaHeading membership function
domainBedaHeading = linspace(-6, 186, 19200)
OT = IT2FS(domainBedaHeading,
 trapezoid_mf, [-6, -5.8, 5.8, 6, 1.],
 trapezoid_mf, [-5.8, -4, 3, 5.8, 0.1]) 
C = IT2FS(domainBedaHeading,
 trapezoid_mf, [6, 10, 173,174,1.],
 trapezoid_mf, [8, 10, 170, 171,0.1]) 
HO = IT2FS(domainBedaHeading,
 trapezoid_mf, [174,175,185,186, 1.],
 trapezoid_mf, [174.5, 175, 180, 185, 0.1])
IT2FS_plot(OT, C, HO, legends=["OT", "C", "HO"], filename="BedaHeading")

#BedaKecepatan membership function
domainBedaKecepatan= linspace(-1., 20, 2000)
Kecil = IT2FS(domainBedaKecepatan,
 trapezoid_mf, [-1,   0,   3.3,   3.5, 1.],
 trapezoid_mf, [0.1, 0.33, 3.23, 3.45, 0.1])
Besar = IT2FS(domainBedaKecepatan,
 trapezoid_mf, [2.5, 3.6, 18, 20, 1.],
 trapezoid_mf, [2.6, 3.7, 17.8, 19, 0.1])
IT2FS_plot(Kecil, Besar, legends=["Kecil", "Besar"], filename="BedaKecepatan")

#KecepatanAngin membership function
domainKecepatanAngin= linspace(0., 27, 2700)
LowRisk =IT2FS(domainKecepatanAngin,
 trapezoid_mf, [0,     1,   14, 15.55,  1],
 trapezoid_mf, [0.5, 0.8, 13.3,  15.3, 0.1])
HighRisk = IT2FS(domainKecepatanAngin,
 trapezoid_mf, [13.61,   15.8,   26,    27,  1],
 trapezoid_mf, [14,      15.7, 26.5,  26.8, 0.1])
IT2FS_plot(LowRisk, HighRisk, legends=["LowRisk", "HighRisk"], filename="KecepatanAngin")

#CurahHujan membership function
domainCurahHujan = linspace(0, 150, 1500)
CR = IT2FS(domainCurahHujan,
 trapezoid_mf, [0, 3, 17, 20, 1.],
 trapezoid_mf, [5, 7, 15, 20, 0.1]) 
HS = IT2FS(domainCurahHujan,
 trapezoid_mf, [15, 20, 50, 55, 1.],
 trapezoid_mf, [17, 23, 47, 53,0.1]) 
HL = IT2FS(domainCurahHujan,
 trapezoid_mf, [45, 50, 145, 150, 1.],
 trapezoid_mf, [48, 50, 143, 148, 0.1])
IT2FS_plot(CR, HS, HL, legends=["CR", "HS", "HL"], filename="CurahHujan")

# output membership function
domainKeputusan=linspace(0,100,10000); 
NoTrans = IT2FS(domainKeputusan,
 tri_mf,[0,0.01,49,  1],
 tri_mf,[0,15.01,48,0.1])
YesTrans = IT2FS(domainKeputusan,
 tri_mf,[49.1,  99, 100,  1],
 tri_mf,[  50,  85,  99,0.1])
IT2FS_plot(NoTrans,YesTrans,legends=["NoTrans","YesTrans"],filename="HasilKeputusan")

# An Interval Type 2 Fuzzy Logic System is created. The variables and output 

# variables are defined. As it can be seen, the system has 5 input and 1 output 

myIT2FLS = IT2FLS()
myIT2FLS.add_input_variable("Jarak") 
myIT2FLS.add_input_variable("BedaHeading") 
myIT2FLS.add_input_variable("BedaKecepatan") 
myIT2FLS.add_input_variable("KecepatanAngin") 
myIT2FLS.add_input_variable("CurahHujan")
myIT2FLS.add_output_variable("HasilKeputusan")

# the fuzzy IF-THEN rules
# 1 
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", OT), ("BedaKecepatan", Kecil), ("KecepatanAngin", LowRisk), ("CurahHujan", CR)], 
                  [("HasilKeputusan", YesTrans)])
# 2
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", OT), ("BedaKecepatan", Kecil), ("KecepatanAngin", LowRisk), ("CurahHujan", HS)], 
                  [("HasilKeputusan", YesTrans)])
# 3
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", OT), ("BedaKecepatan", Kecil), ("KecepatanAngin", LowRisk), ("CurahHujan", HL)], 
                  [("HasilKeputusan", NoTrans)])
# 4
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", OT), ("BedaKecepatan", Kecil), ("KecepatanAngin", HighRisk), ("CurahHujan", CR)], 
                  [("HasilKeputusan", NoTrans)])
# 5
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", OT), ("BedaKecepatan", Kecil), ("KecepatanAngin", HighRisk), ("CurahHujan", HS)], 
                  [("HasilKeputusan", NoTrans)])
# 6
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", OT), ("BedaKecepatan", Kecil), ("KecepatanAngin", HighRisk), ("CurahHujan", HL)], 
                  [("HasilKeputusan", NoTrans)])
# 7
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", OT), ("BedaKecepatan", Besar), ("KecepatanAngin", LowRisk), ("CurahHujan", CR)], 
                  [("HasilKeputusan", NoTrans)])
# 8
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", OT), ("BedaKecepatan", Besar), ("KecepatanAngin", LowRisk), ("CurahHujan", HS)], 
                  [("HasilKeputusan", NoTrans)])
# 9
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", OT), ("BedaKecepatan", Besar), ("KecepatanAngin", LowRisk), ("CurahHujan", HL)], 
                  [("HasilKeputusan", NoTrans)])
# 10
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", OT), ("BedaKecepatan", Besar), ("KecepatanAngin", HighRisk), ("CurahHujan", CR)], 
                  [("HasilKeputusan", NoTrans)])
# 11 
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", OT), ("BedaKecepatan", Besar), ("KecepatanAngin", HighRisk), ("CurahHujan", HS)], 
                  [("HasilKeputusan", NoTrans)])
# 12
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", OT), ("BedaKecepatan", Besar), ("KecepatanAngin", HighRisk), ("CurahHujan", HL)], 
                  [("HasilKeputusan", NoTrans)])
# 13
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", C), ("BedaKecepatan", Kecil), ("KecepatanAngin", LowRisk), ("CurahHujan", CR)], 
                  [("HasilKeputusan", NoTrans)])
# 14
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", C), ("BedaKecepatan", Kecil), ("KecepatanAngin", LowRisk), ("CurahHujan", HS)], 
                  [("HasilKeputusan", NoTrans)])
# 15
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", C), ("BedaKecepatan", Kecil), ("KecepatanAngin", LowRisk), ("CurahHujan", HL)], 
                  [("HasilKeputusan", NoTrans)])
# 16
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", C), ("BedaKecepatan", Kecil), ("KecepatanAngin", HighRisk), ("CurahHujan", CR)], 
                  [("HasilKeputusan", NoTrans)])
# 17
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", C), ("BedaKecepatan", Kecil), ("KecepatanAngin", HighRisk), ("CurahHujan", HS)], 
                  [("HasilKeputusan", NoTrans)])
# 18
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", C), ("BedaKecepatan", Kecil), ("KecepatanAngin", HighRisk), ("CurahHujan", HL)], 
                  [("HasilKeputusan", NoTrans)])
# 19
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", C), ("BedaKecepatan", Besar), ("KecepatanAngin", LowRisk), ("CurahHujan", CR)], 
                  [("HasilKeputusan", NoTrans)])
# 20
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", C), ("BedaKecepatan", Besar), ("KecepatanAngin", LowRisk), ("CurahHujan", HS)], 
                  [("HasilKeputusan", NoTrans)])
# 21
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", C), ("BedaKecepatan", Besar), ("KecepatanAngin", LowRisk), ("CurahHujan", HL)], 
                  [("HasilKeputusan", NoTrans)])
# 22
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", C), ("BedaKecepatan", Besar), ("KecepatanAngin", HighRisk), ("CurahHujan", CR)], 
                  [("HasilKeputusan", NoTrans)])
# 23
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", C), ("BedaKecepatan", Besar), ("KecepatanAngin", HighRisk), ("CurahHujan", HS)], 
                  [("HasilKeputusan", NoTrans)])
# 24
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", C), ("BedaKecepatan", Besar), ("KecepatanAngin", HighRisk), ("CurahHujan", HL)], 
                  [("HasilKeputusan", NoTrans)])
# 25
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", HO), ("BedaKecepatan", Kecil), ("KecepatanAngin", LowRisk), ("CurahHujan", CR)], 
                  [("HasilKeputusan", YesTrans)])
# 26
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", HO), ("BedaKecepatan", Kecil), ("KecepatanAngin", LowRisk), ("CurahHujan", HS)], 
                  [("HasilKeputusan", YesTrans)])
# 27
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", HO), ("BedaKecepatan", Kecil), ("KecepatanAngin", LowRisk), ("CurahHujan", HL)], 
                  [("HasilKeputusan", NoTrans)])
# 28
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", HO), ("BedaKecepatan", Kecil), ("KecepatanAngin", HighRisk), ("CurahHujan", CR)], 
                  [("HasilKeputusan", NoTrans)])
# 29
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", HO), ("BedaKecepatan", Kecil), ("KecepatanAngin", HighRisk), ("CurahHujan", HS)], 
                  [("HasilKeputusan", NoTrans)])
# 30
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", HO), ("BedaKecepatan", Kecil), ("KecepatanAngin", HighRisk), ("CurahHujan", HL)], 
                  [("HasilKeputusan", NoTrans)])
# 31
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", HO), ("BedaKecepatan", Besar), ("KecepatanAngin", LowRisk), ("CurahHujan", CR)], 
                  [("HasilKeputusan", NoTrans)])
# 32
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", HO), ("BedaKecepatan", Besar), ("KecepatanAngin", LowRisk), ("CurahHujan", HS)], 
                  [("HasilKeputusan", NoTrans)])
# 33
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", HO), ("BedaKecepatan", Besar), ("KecepatanAngin", LowRisk), ("CurahHujan", HL)], 
                  [("HasilKeputusan", NoTrans)])
# 34
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", HO), ("BedaKecepatan", Besar), ("KecepatanAngin", HighRisk), ("CurahHujan", CR)], 
                  [("HasilKeputusan", NoTrans)])
# 35
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", HO), ("BedaKecepatan", Besar), ("KecepatanAngin", HighRisk), ("CurahHujan", HS)], 
                  [("HasilKeputusan", NoTrans)])
# 36
myIT2FLS.add_rule([("Jarak", Dekat), ("BedaHeading", HO), ("BedaKecepatan", Besar), ("KecepatanAngin", HighRisk), ("CurahHujan", HL)], 
                  [("HasilKeputusan", NoTrans)])
# 37 
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", OT), ("BedaKecepatan", Kecil), ("KecepatanAngin", LowRisk), ("CurahHujan", CR)], 
                  [("HasilKeputusan", YesTrans)])
# 38
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", OT), ("BedaKecepatan", Kecil), ("KecepatanAngin", LowRisk), ("CurahHujan", HS)], 
                  [("HasilKeputusan", YesTrans)])
# 39
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", OT), ("BedaKecepatan", Kecil), ("KecepatanAngin", LowRisk), ("CurahHujan", HL)], 
                  [("HasilKeputusan", NoTrans)])
# 40
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", OT), ("BedaKecepatan", Kecil), ("KecepatanAngin", HighRisk), ("CurahHujan", CR)], 
                  [("HasilKeputusan", NoTrans)])
# 41
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", OT), ("BedaKecepatan", Kecil), ("KecepatanAngin", HighRisk), ("CurahHujan", HS)], 
                  [("HasilKeputusan", NoTrans)])
# 42
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", OT), ("BedaKecepatan", Kecil), ("KecepatanAngin", HighRisk), ("CurahHujan", HL)], 
                  [("HasilKeputusan", NoTrans)])
# 43
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", OT), ("BedaKecepatan", Besar), ("KecepatanAngin", LowRisk), ("CurahHujan", CR)], 
                  [("HasilKeputusan", NoTrans)])
# 44
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", OT), ("BedaKecepatan", Besar), ("KecepatanAngin", LowRisk), ("CurahHujan", HS)], 
                  [("HasilKeputusan", NoTrans)])
# 45
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", OT), ("BedaKecepatan", Besar), ("KecepatanAngin", LowRisk), ("CurahHujan", HL)], 
                  [("HasilKeputusan", NoTrans)])
# 46
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", OT), ("BedaKecepatan", Besar), ("KecepatanAngin", HighRisk), ("CurahHujan", CR)], 
                  [("HasilKeputusan", NoTrans)])
# 47 
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", OT), ("BedaKecepatan", Besar), ("KecepatanAngin", HighRisk), ("CurahHujan", HS)], 
                  [("HasilKeputusan", NoTrans)])
# 48
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", OT), ("BedaKecepatan", Besar), ("KecepatanAngin", HighRisk), ("CurahHujan", HL)], 
                  [("HasilKeputusan", NoTrans)])
# 49
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", C), ("BedaKecepatan", Kecil), ("KecepatanAngin", LowRisk), ("CurahHujan", CR)], 
                  [("HasilKeputusan", NoTrans)])
# 50
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", C), ("BedaKecepatan", Kecil), ("KecepatanAngin", LowRisk), ("CurahHujan", HS)], 
                  [("HasilKeputusan", NoTrans)])
# 51
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", C), ("BedaKecepatan", Kecil), ("KecepatanAngin", LowRisk), ("CurahHujan", HL)], 
                  [("HasilKeputusan", NoTrans)])
# 52
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", C), ("BedaKecepatan", Kecil), ("KecepatanAngin", HighRisk), ("CurahHujan", CR)], 
                  [("HasilKeputusan", NoTrans)])
# 53
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", C), ("BedaKecepatan", Kecil), ("KecepatanAngin", HighRisk), ("CurahHujan", HS)], 
                  [("HasilKeputusan", NoTrans)])
# 54
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", C), ("BedaKecepatan", Kecil), ("KecepatanAngin", HighRisk), ("CurahHujan", HL)], 
                  [("HasilKeputusan", NoTrans)])
# 55
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", C), ("BedaKecepatan", Besar), ("KecepatanAngin", LowRisk), ("CurahHujan", CR)], 
                  [("HasilKeputusan", NoTrans)])
# 56
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", C), ("BedaKecepatan", Besar), ("KecepatanAngin", LowRisk), ("CurahHujan", HS)], 
                  [("HasilKeputusan", NoTrans)])
# 57
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", C), ("BedaKecepatan", Besar), ("KecepatanAngin", LowRisk), ("CurahHujan", HL)], 
                  [("HasilKeputusan", NoTrans)])
# 58
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", C), ("BedaKecepatan", Besar), ("KecepatanAngin", HighRisk), ("CurahHujan", CR)], 
                  [("HasilKeputusan", NoTrans)])
# 59
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", C), ("BedaKecepatan", Besar), ("KecepatanAngin", HighRisk), ("CurahHujan", HS)], 
                  [("HasilKeputusan", NoTrans)])
# 60
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", C), ("BedaKecepatan", Besar), ("KecepatanAngin", HighRisk), ("CurahHujan", HL)], 
                  [("HasilKeputusan", NoTrans)])
# 61
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", HO), ("BedaKecepatan", Kecil), ("KecepatanAngin", LowRisk), ("CurahHujan", CR)], 
                  [("HasilKeputusan", YesTrans)])
# 62
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", HO), ("BedaKecepatan", Kecil), ("KecepatanAngin", LowRisk), ("CurahHujan", HS)], 
                  [("HasilKeputusan", YesTrans)])
# 63
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", HO), ("BedaKecepatan", Kecil), ("KecepatanAngin", LowRisk), ("CurahHujan", HL)], 
                  [("HasilKeputusan", NoTrans)])
# 64
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", HO), ("BedaKecepatan", Kecil), ("KecepatanAngin", HighRisk), ("CurahHujan", CR)], 
                  [("HasilKeputusan", NoTrans)])
# 65
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", HO), ("BedaKecepatan", Kecil), ("KecepatanAngin", HighRisk), ("CurahHujan", HS)], 
                  [("HasilKeputusan", NoTrans)])
# 66
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", HO), ("BedaKecepatan", Kecil), ("KecepatanAngin", HighRisk), ("CurahHujan", HL)], 
                  [("HasilKeputusan", NoTrans)])
# 67
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", HO), ("BedaKecepatan", Besar), ("KecepatanAngin", LowRisk), ("CurahHujan", CR)], 
                  [("HasilKeputusan", NoTrans)])
# 68
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", HO), ("BedaKecepatan", Besar), ("KecepatanAngin", LowRisk), ("CurahHujan", HS)], 
                  [("HasilKeputusan", NoTrans)])
# 69
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", HO), ("BedaKecepatan", Besar), ("KecepatanAngin", LowRisk), ("CurahHujan", HL)], 
                  [("HasilKeputusan", NoTrans)])
# 70
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", HO), ("BedaKecepatan", Besar), ("KecepatanAngin", HighRisk), ("CurahHujan", CR)], 
                  [("HasilKeputusan", NoTrans)])
# 71
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", HO), ("BedaKecepatan", Besar), ("KecepatanAngin", HighRisk), ("CurahHujan", HS)], 
                  [("HasilKeputusan", NoTrans)])
# 72
myIT2FLS.add_rule([("Jarak", Jauh), ("BedaHeading", HO), ("BedaKecepatan", Besar), ("KecepatanAngin", HighRisk), ("CurahHujan", HL)], 
                  [("HasilKeputusan", NoTrans)])

it2out, tr=myIT2FLS.evaluate({"Jarak":5, "BedaHeading":0, "BedaKecepatan":2,"KecepatanAngin":5,"CurahHujan":12}, 
min_t_norm,max_s_norm, domainKeputusan,
 method="Centroid", algorithm="KM")

it2out["HasilKeputusan"].plot(filename="hasil Identifikasi IUU")
TR_plot(domainKeputusan, tr["HasilKeputusan"], filename="hasil Identifikasi IUU")
print((crisp(tr["HasilKeputusan"])))
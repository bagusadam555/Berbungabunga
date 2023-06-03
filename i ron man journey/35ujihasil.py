from pyit2fls import Mamdani, rtri_mf,ltri_mf,IT2FS, IT2FLS, trapezoid_mf, tri_mf, IT2FS_plot, min_t_norm, max_s_norm, TR_plot, crisp
from numpy import linspace, meshgrid, zeros
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

#Defining an interval type 2 fuzzy set with trapzeoidal and tringular mf


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
domainBedaKecepatan= linspace(0., 20, 2000)
Kecil = IT2FS(domainBedaKecepatan,
 trapezoid_mf, [0,   0.3,   3.3,   3.5, 1.],
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


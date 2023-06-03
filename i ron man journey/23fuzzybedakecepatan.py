from pyit2fls import Mamdani, rtri_mf,ltri_mf,IT2FS, IT2FLS, trapezoid_mf, tri_mf, IT2FS_plot, min_t_norm, max_s_norm, TR_plot, crisp
from numpy import linspace, meshgrid, zeros
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

#domain BedaKecepatan membership function
domainBedaKecepatan= linspace(0., 20, 2000)
Kecil = IT2FS(domainBedaKecepatan,
 trapezoid_mf, [0, 0.3,   3.3,   3.5, 1.],
 trapezoid_mf, [0.1, 0.33, 3.23, 3.45, 0.1])
Besar = IT2FS(domainBedaKecepatan,
 trapezoid_mf, [2.5, 3.6, 18, 20, 1.],
 trapezoid_mf, [2.6, 3.7, 17.8, 19, 0.1])
IT2FS_plot(Kecil, Besar, legends=["Kecil", "Besar"], filename="BedaKecepatan")

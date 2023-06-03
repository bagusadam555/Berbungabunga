from pyit2fls import Mamdani, rtri_mf,ltri_mf,IT2FS, IT2FLS, trapezoid_mf, tri_mf, IT2FS_plot, min_t_norm, max_s_norm, TR_plot, crisp
from numpy import linspace, meshgrid, zeros
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


domainJarak= linspace(0., 2000, 6000)
Dekat = IT2FS(domainJarak,
 trapezoid_mf, [0, 200,   780,   850, 1.],
 trapezoid_mf, [1, 250, 750, 830, 0.1])
Jauh = IT2FS(domainJarak,
 trapezoid_mf, [800, 1100, 1850,2000, 1.],
 trapezoid_mf, [850, 1100, 1800, 1950, 0.1])
IT2FS_plot(Dekat, Jauh, legends=["Dekat", "Jauh"], filename="Jarak")
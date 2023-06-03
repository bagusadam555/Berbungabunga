from pyit2fls import Mamdani, rtri_mf,ltri_mf,IT2FS, IT2FLS, trapezoid_mf, tri_mf, IT2FS_plot, min_t_norm, max_s_norm, TR_plot, crisp
from numpy import linspace, meshgrid, zeros
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

domain_delD = linspace(0., 55, 300)
Near = IT2FS(domain_delD,
 trapezoid_mf, [0, 5, 13, 22, 1.],
 trapezoid_mf, [5,5.5, 10.5, 17, 1])
Far = IT2FS(domain_delD,
 trapezoid_mf, [39, 43, 53,55 , 1.],
 trapezoid_mf, [34, 40,49, 50, 1])
IT2FS_plot(Near, Far, legends=["Near", "Far"], filename="delD")

domainJarak= linspace(0., 100, 300)
Dekat = IT2FS(domainJarak,
 trapezoid_mf, [0, 0,   4.8,   5, 1.],
 trapezoid_mf, [1, 2.5, 4.5, 4.8, 0.2])
Jauh = IT2FS(domainJarak,
 trapezoid_mf, [6, 10, 90,100, 1.],
 trapezoid_mf, [8, 10, 80, 95, 0.1])
IT2FS_plot(Dekat, Jauh, legends=["Dekat", "Jauh"], filename="Jarak")
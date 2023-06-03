from pyit2fls import Mamdani, rtri_mf,ltri_mf,IT2FS, IT2FLS, trapezoid_mf, tri_mf, IT2FS_plot, min_t_norm, max_s_norm, TR_plot, crisp
from numpy import linspace, meshgrid, zeros
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

#domain delHead membership function
domain_delHead = linspace(-6, 186, 19200)
OT = IT2FS(domain_delHead,
 trapezoid_mf, [-6, -5, 5, 6, 1.],
 trapezoid_mf, [-3, 0, 3, 4, 1]) 
C = IT2FS(domain_delHead,
 trapezoid_mf, [9,10,173,174,1.],
 trapezoid_mf, [6, 7, 170, 171,1]) 
HO = IT2FS(domain_delHead,
 trapezoid_mf, [174,175,185,186, 1.],
 trapezoid_mf, [150, 155, 160, 165, 1])
IT2FS_plot(OT, C, HO, legends=["OT", "C", "HO"], filename="delHead")

#domain BedaHeading membership function
domainBedaHeading = linspace(-6, 186, 19200)
OT = IT2FS(domainBedaHeading,
 trapezoid_mf, [-6, -5.8, 5.8, 6, 1.],
 trapezoid_mf, [-5.8, -4, 3, 5.8, 0.1]) 
CR = IT2FS(domainBedaHeading,
 trapezoid_mf, [6, 10, 173,174,1.],
 trapezoid_mf, [8, 10, 170, 171,0.1]) 
HO = IT2FS(domainBedaHeading,
 trapezoid_mf, [174,175,185,186, 1.],
 trapezoid_mf, [174.5, 175, 180, 185, 0.1])
IT2FS_plot(OT, CR, HO, legends=["OT", "CR", "HO"], filename="BedaHeading")
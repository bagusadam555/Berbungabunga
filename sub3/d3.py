from pyit2fls import Mamdani, rtri_mf,ltri_mf,IT2FS, IT2FLS, trapezoid_mf, tri_mf, IT2FS_plot, min_t_norm, max_s_norm, TR_plot, crisp
from numpy import linspace, meshgrid, zeros
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
#Defining an interval type 2 fuzzy set with trapzeoidal and tringular mf
# delD membership function
domain_delD = linspace(0., 55, 300)
Near = IT2FS(domain_delD,
 trapezoid_mf, [0, 5, 13, 22, 1.],
 trapezoid_mf, [5,5.5, 10.5, 17, 1])
Far = IT2FS(domain_delD,
 trapezoid_mf, [39, 43, 53,55 , 1.],
 trapezoid_mf, [34, 40,49, 50, 1])
IT2FS_plot(Near, Far, legends=["Near", "Far"], filename="delD")
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
# delV membership function
domain_delV = linspace(0, 5, 500)
kecil = IT2FS(domain_delV,
 trapezoid_mf, [0,0.01,0.3,0.5,1],
 tri_mf, [0.2,0.21,0.3, 1])
besar = IT2FS(domain_delV,
 trapezoid_mf, [0.55, 4.7, 4.99, 5, 1],
 tri_mf, [0.35, 4.5, 4.71, 1])
IT2FS_plot(kecil, besar, legends=["kecil", "besar"], filename="delV")
# membership function
domain_IdentificationResult=linspace(0,100,10000); NoTrans = IT2FS(domain_IdentificationResult,
 tri_mf,[0,0.01,50,1],
 tri_mf,[0,0.01,40,0.8])
YesTrans = IT2FS(domain_IdentificationResult,
 tri_mf,[50, 99,100,1],
 tri_mf,[60,99.99,99,0.8])
IT2FS_plot(NoTrans,YesTrans,legends=["NoTrans","YesTrans"],filename="IdentificationResult")
# An Interval Type 2 Fuzzy Logic System is created. The variables and output 
# variables are defined. As it can be seen, the system has 3 input and 1 output 
myIT2FLS = IT2FLS()
myIT2FLS.add_input_variable("delD") 
myIT2FLS.add_input_variable("delHead") 
myIT2FLS.add_input_variable("delV") 
myIT2FLS.add_output_variable("Result")
# the fuzzy IF-THEN rules
# 1
myIT2FLS.add_rule([("delD", Near),("delHead", OT), ("delV", 
kecil)], [("Result", YesTrans)])
# 2
myIT2FLS.add_rule([("delD", Near),("delHead", OT), ("delV", 
besar)], [("Result", NoTrans)])
# 3
myIT2FLS.add_rule([("delD", Near),("delHead", C), ("delV", 
kecil)], [("Result", YesTrans)])
# 4
myIT2FLS.add_rule([("delD", Near),("delHead", C), ("delV", 
besar)], [("Result", NoTrans)])
# 5
myIT2FLS.add_rule([("delD", Near),("delHead", HO), ("delV", 
kecil)], [("Result", YesTrans)])
# 6
myIT2FLS.add_rule([("delD", Near),("delHead", HO), ("delV", 
besar)], [("Result", NoTrans)])
# 7
myIT2FLS.add_rule([("delD", Far),("delHead", OT), ("delV", 
kecil)], [("Result", YesTrans)])
# 8
myIT2FLS.add_rule([("delD", Far),("delHead", OT), ("delV", 
besar)], [("Result", NoTrans)])
# 9
myIT2FLS.add_rule([("delD", Far),("delHead", C), ("delV", kecil)], 
[("Result", YesTrans)])
# 10
myIT2FLS.add_rule([("delD", Far),("delHead", C), ("delV", besar)], 
[("Result", NoTrans)])
# 11 
myIT2FLS.add_rule([("delD", Far),("delHead", HO), ("delV", kecil)], [("Result", YesTrans)])
# 12
myIT2FLS.add_rule([("delD", Far),("delHead", HO), ("delV", 
besar)], [("Result", YesTrans)])

def decisionfinal(delD, delHead, delV):
    it2out, tr=myIT2FLS.evaluate({"delD":delD, "delHead":delHead, "delV":delV}, 
    min_t_norm,max_s_norm, domain_IdentificationResult,
    method="Centroid", algorithm="KM")
    it2out["Result"].plot(filename="hasil selection")
    TR_plot(domain_IdentificationResult, tr["Result"], filename="hasilselection")
    print((crisp(tr["Result"])))
    


from random import uniform
from time import perf_counter
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import getdist
from getdist import plots

c = 299_792.458 # km/s

class SN:
    def __init__(self, mu, sigma_mu, z=None, logcz=None, name=""):
        self.name = name
        if logcz is not None:
            self.z = 10**logcz/c
        else:
            self.z = z
        self.mu = mu
        self.sigma_mu = sigma_mu
        self.DL = 10**((self.mu - 25)/5) # in Mpc
        self.sigma_DL = 10**((self.mu - 25)/5)*np.log(10)/5*sigma_mu # in Mpc

mlcs = [
    SN(logcz=3.734, mu=34.72, sigma_mu=0.16, name="1992bo"),
    SN(logcz=3.779, mu=34.87, sigma_mu=0.11, name="1992bc"),
    SN(logcz=4.481, mu=38.41, sigma_mu=0.15, name="1992aq"),
    SN(logcz=4.350, mu=37.80, sigma_mu=0.17, name="1992ae"),
    SN(logcz=3.896, mu=35.76, sigma_mu=0.13, name="1992P"),
    SN(logcz=4.178, mu=36.53, sigma_mu=0.15, name="1990af"),
    SN(logcz=3.859, mu=35.39, sigma_mu=0.18, name="1994M"),
    SN(logcz=3.685, mu=34.27, sigma_mu=0.12, name="1994S"),
    SN(logcz=4.030, mu=36.19, sigma_mu=0.21, name="1994T"),
    SN(logcz=3.398, mu=33.01, sigma_mu=0.13, name="1995D"),
    SN(logcz=3.547, mu=33.60, sigma_mu=0.17, name="1995E"),
    SN(logcz=4.166, mu=36.85, sigma_mu=0.13, name="1995ac"),
    SN(logcz=3.820, mu=35.15, sigma_mu=0.16, name="1995ak"),
    SN(logcz=3.679, mu=34.15, sigma_mu=0.19, name="1995bd"),
    SN(logcz=3.924, mu=35.98, sigma_mu=0.20, name="1996C"),
    SN(logcz=4.572, mu=39.01, sigma_mu=0.13, name="1996ab"),
    SN(logcz=3.891, mu=35.37, sigma_mu=0.23, name="1992ag"),
    SN(logcz=3.625, mu=33.92, sigma_mu=0.23, name="1992al"),
    SN(logcz=4.024, mu=36.26, sigma_mu=0.23, name="1992bg"),
    SN(logcz=4.130, mu=36.91, sigma_mu=0.23, name="1992bh"),
    SN(logcz=4.111, mu=36.26, sigma_mu=0.23, name="1992bl"),
    SN(logcz=4.379, mu=37.65, sigma_mu=0.23, name="1992bp"),
    SN(logcz=4.418, mu=38.21, sigma_mu=0.23, name="1992br"),
    SN(logcz=4.283, mu=37.61, sigma_mu=0.23, name="1992bs"),
    SN(logcz=3.871, mu=35.20, sigma_mu=0.23, name="1993H"),
    SN(logcz=4.189, mu=37.03, sigma_mu=0.23, name="1993O"),
    SN(logcz=4.177, mu=36.80, sigma_mu=0.23, name="1993ag"),
]

highz = [
    SN(z=0.43, mu=41.74, sigma_mu=0.28, name="1996E"),
    SN(z=0.62, mu=42.98, sigma_mu=0.17, name="1996H"),
    SN(z=0.57, mu=42.76, sigma_mu=0.19, name="1996I"),
    SN(z=0.30, mu=41.38, sigma_mu=0.24, name="1996J"),
    SN(z=0.38, mu=41.63, sigma_mu=0.20, name="1996K"),
    SN(z=0.43, mu=42.55, sigma_mu=0.25, name="1996U"),
    SN(z=0.44, mu=41.95, sigma_mu=0.17, name="1997ce"),
    SN(z=0.50, mu=42.40, sigma_mu=0.17, name="1997cj"),
    SN(z=0.97, mu=44.39, sigma_mu=0.30, name="1997ck"),
    SN(z=0.45, mu=42.45, sigma_mu=0.17, name="1995K"),
]

all = mlcs + highz
zs = np.array([sn.z for sn in all])
mus = np.array([sn.mu for sn in all])
sigmas = np.array([sn.sigma_mu for sn in all])

sigma_vel_disp_lowz = 5/np.log(10) * 200 / 299_792.458
sigma_vel_disp_highz = 5/np.log(10) * np.sqrt((200**2 + 2500**2)) / 299_792.458
sigma_vel_disp = np.array([sigma_vel_disp_lowz/z if z < 0.2 else sigma_vel_disp_highz/z for z in zs])
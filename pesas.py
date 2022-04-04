import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df1 = pd.read_csv("datos_pesas_r1.csv")
df2 = pd.read_csv("datos_pesas_r2.csv")


# Now an errorbar must be done to not only show the measurements, but also the error margin for each measure done.
def errorbar_r1():

    x = df1["mass"]
    y = df1["longitude_r1"]
    xerr = df1["mass_error"]
    yerr = df1["longitude_error"]
    
    fig = plt.subplots()
    
    plt.errorbar(x, y, yerr, xerr)
    plt.xlabel('Mass (g)')
    plt.ylabel('Longitude (cm)')

    plt.savefig('pesas_r1.png')
    return fig

errorbar_r1()


def errorbar_r2():

    x = df2["mass"]
    y = df2["longitude_r2"]
    xerr = df2["mass_error"]
    yerr = df2["longitude_error"]
    
    fig = plt.subplots()
    
    plt.errorbar(x, y, yerr, xerr)
    plt.xlabel('Mass (g)')
    plt.ylabel('Longitude (cm)')

    plt.savefig('pesas_r2.png')
    return fig

errorbar_r2()
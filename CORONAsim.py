import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family='BIZ UDGothic')
fig=plt.figure()

MODE=st.sidebar.radio("MODE",["u-E","x-KE"])
d=st.sidebar.slider("電極間距離(mm)",0.1,10.0,3.0,0.1)/1000
V=st.sidebar.slider("印加電圧(V)",0,5000,3000,50)
focus=st.sidebar.checkbox("focus")
if focus==True:
    m=95.0
else:
    m=0.1
v0=st.sidebar.slider("尖度(%)",m,99.9,98.1,0.1)/100*np.pi
lm=375/(10**9)

u=np.linspace(-2,2,101)
v=np.linspace(0,v0,101)
u2=[-1,0,1]
v2=[v0/4,v0/2,v0*3/4]
E=((2*np.sin(v0/2))/(d*((np.exp(u)+np.exp(-u)+2*np.cos(v0))**(1/2))))*(V/np.cos(v0/2))/(np.log((np.cos(v0/4)+np.sin(v0/4))/(np.cos(v0/4)-np.sin(v0/4))))

for uu in u2:
    x=d*np.cos(v/2)*(np.exp(uu/2)-np.exp(-uu/2))/(2*np.sin(v0/2))
    y=d*np.sin(v/2)*(np.exp(uu/2)+np.exp(-uu/2))/(2*np.sin(v0/2))
    plt.plot(x*1000,y*1000,c="k",ls="--")

for vv in v2:
    x=d*np.cos(vv/2)*(np.exp(u/2)-np.exp(-u/2))/(2*np.sin(v0/2))
    y=d*np.sin(vv/2)*(np.exp(u/2)+np.exp(-u/2))/(2*np.sin(v0/2))
    plt.plot(x*1000,y*1000,c="k",ls="--")

x=d*np.cos(v0/2)*(np.exp(u/2)-np.exp(-u/2))/(2*np.sin(v0/2))
y=d*np.sin(v0/2)*(np.exp(u/2)+np.exp(-u/2))/(2*np.sin(v0/2))
plt.plot(x*1000,y*1000,c="r",label="needle")
plt.axhline(y=0,c="g",label="plane")
plt.xlim(-3,3)
plt.xlabel("x(mm)")
plt.ylabel("y(mm)")
plt.legend()
st.pyplot(fig)

fig=plt.figure()
if MODE=="u-E":
    plt.plot(u,E,"-o",ms=3)
    plt.xlabel("u")
    plt.ylabel("E(V/m)")
else:
    x=1000*d*(np.exp(u/2)-np.exp(-u/2))/(2*np.sin(v0/2))
    KE=E*lm
    plt.axhline(y=9.8,c="k",ls="--")
    plt.plot(x,KE,"-o",ms=3)
    plt.xlabel("x(mm)")
    plt.ylabel("KE(eV)")
    plt.xlim(-3,3)
st.pyplot(fig)

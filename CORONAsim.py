import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family='BIZ UDGothic')
d=st.sidebar.slider("電極間距離(mm)",0.1,10.0,3.0,0.1)/1000   #電極間距離
V=st.sidebar.slider("印加電圧(V)",0,5000,3000,50)             #印加電圧
v0=st.sidebar.slider("尖度(%)",0.1,99.9,98.1,0.1)/100*np.pi   #尖度
lm=375/(10**9)                                                #平均自由行程
fig=plt.figure(figsize=(12,5))
ax1=fig.add_subplot(1,2,1)
ax2=fig.add_subplot(1,2,2)

#ax1:幾何学プレビュー
u=np.linspace(-2,2,101)
v=np.linspace(0,v0,101)
u2=[-1,0,1]
v2=[v0/4,v0/2,v0*3/4]

for uu in u2:
    x=d*np.cos(v/2)*(np.exp(uu/2)-np.exp(-uu/2))/(2*np.sin(v0/2))
    y=d*np.sin(v/2)*(np.exp(uu/2)+np.exp(-uu/2))/(2*np.sin(v0/2))
    ax1.plot(x*1000,y*1000,c="k",ls="--")#電気力線の描画

for vv in v2:
    x=d*np.cos(vv/2)*(np.exp(u/2)-np.exp(-u/2))/(2*np.sin(v0/2))
    y=d*np.sin(vv/2)*(np.exp(u/2)+np.exp(-u/2))/(2*np.sin(v0/2))
    ax1.plot(x*1000,y*1000,c="k",ls="--")#等電位線の描画

x=d*np.cos(v0/2)*(np.exp(u/2)-np.exp(-u/2))/(2*np.sin(v0/2))
y=d*np.sin(v0/2)*(np.exp(u/2)+np.exp(-u/2))/(2*np.sin(v0/2))
ax1.plot(x*1000,y*1000,c="r",label="needle")#針電極の描画
ax1.axhline(y=0,c="g",label="plane")#平面電極の描画
ax1.set_xlim(-d*1000,d*1000)
ax1.set_xlabel("x(mm)")
ax1.set_ylabel("y(mm)")
ax1.legend()

#ax2:電子の運動エネルギーの計算とプロット
E=((2*np.sin(v0/2))/(d*((np.exp(u)+np.exp(-u)+2*np.cos(v0))**(1/2))))*(V/np.cos(v0/2))/(np.log((np.cos(v0/4)+np.sin(v0/4))/(np.cos(v0/4)-np.sin(v0/4))))
x=1000*d*(np.exp(u/2)-np.exp(-u/2))/(2*np.sin(v0/2))
KE=E*lm
ax2.axhline(y=9.8,c="k",ls="--")
ax2.plot(x,KE,"-o",ms=3)
ax2.set_xlabel("x(mm)")
ax2.set_ylabel("KE(eV)")
ax2.set_xlim(-3,3)
st.pyplot(fig)

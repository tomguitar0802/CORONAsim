import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family='BIZ UDGothic')
st.sidebar.write("放電環境の設定")
d=st.sidebar.slider("電極間距離(mm)",0.1,10.0,3.0,0.1)/1000   #電極間距離
V=st.sidebar.slider("印加電圧(V)",0,5000,3000,50)             #印加電圧
m=0.1                                                         #最小v
v0=st.sidebar.slider("尖度(%)",m,99.9,98.1916,0.1)/100*np.pi     #尖度
lm=375/(10**9)                                                #平均自由行程
st.sidebar.write("サンプルポイントの設定")
u_sample=st.sidebar.slider("u",-1.75,1.75,0.0,0.05)
v_sample=st.sidebar.slider("v",m,99.9,98.1916,0.1)/100*np.pi

#幾何学プレビュー
fig=plt.figure()
u=np.linspace(-2,2,101)
v=np.linspace(0,v0,101)
u2=[-1.75,-1.25,-0.65,0,0.65,1.25,1.75]
v2=[v0/4,v0/2,v0*3/4]

#電気力線の描画
for uu in u2:
    x=d*np.cos(v/2)*(np.exp(uu/2)-np.exp(-uu/2))/(2*np.sin(v0/2))
    y=d*np.sin(v/2)*(np.exp(uu/2)+np.exp(-uu/2))/(2*np.sin(v0/2))
    plt.plot(x*1000,y*1000,c="k",ls="--")

#等電位線の描画
for vv in v2:
    x=d*np.cos(vv/2)*(np.exp(u/2)-np.exp(-u/2))/(2*np.sin(v0/2))
    y=d*np.sin(vv/2)*(np.exp(u/2)+np.exp(-u/2))/(2*np.sin(v0/2))
    plt.plot(x*1000,y*1000,c="k")

#電極の描画
x=d*np.cos(v0/2)*(np.exp(u/2)-np.exp(-u/2))/(2*np.sin(v0/2))
y=d*np.sin(v0/2)*(np.exp(u/2)+np.exp(-u/2))/(2*np.sin(v0/2))
plt.plot(x*1000,y*1000,c="r",label="needle")
plt.axhline(y=0,c="g",label="plane")

#サンプルポイントの描画
x_sample=d*np.cos(v_sample/2)*(np.exp(u_sample/2)-np.exp(-u_sample/2))/(2*np.sin(v0/2))
y_sample=d*np.sin(v_sample/2)*(np.exp(u_sample/2)+np.exp(-u_sample/2))/(2*np.sin(v0/2))
plt.scatter(x_sample*1000,y_sample*1000,c="k")

plt.xlim(-d*1000,d*1000)
plt.xlabel("x(mm)")
plt.ylabel("y(mm)")
plt.legend()
st.pyplot(fig)

#電界強度・電子の運動エネルギーの計算とプロット
fig=plt.figure()

E=((2*np.sin(v0/2))/(d*((np.exp(u)+np.exp(-u)+2*np.cos(v0))**(1/2))))*(V/np.cos(v0/2))/(np.log((np.cos(v0/4)+np.sin(v0/4))/(np.cos(v0/4)-np.sin(v0/4))))
x=1000*d*(np.exp(u/2)-np.exp(-u/2))/(2*np.sin(v0/2))
KE=E*lm
#plt.axhline(y=9.8,c="k",ls="--")
plt.plot(x,KE,"-o",ms=3)
plt.xlabel("x(mm)")
plt.ylabel("KE(eV)")
plt.xlim(-3,3)
st.pyplot(fig)

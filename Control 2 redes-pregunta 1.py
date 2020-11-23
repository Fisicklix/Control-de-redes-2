import numpy as np
import matplotlib.pyplot as plt
#planteamiento del periodo
periodo=10
#Definicion del A
A=1
#intervalo a trabajoar
intervalo=5
#periodo
periodo=2*intervalo
#funciones
funcion=[]
tiempo=[]
t=-intervalo
while(t<intervalo):
	tiempo.append(t)
	if(t>=-1 and t<=0):
		funcion.append(A*t+A)
	elif(t>0 and t<=4):
		funcion.append(((-A*t)/4)+A)
	else:
		funcion.append(0)
	
	t+=1/1000
#largo de los vectores
N=len(tiempo)
#conversion a arrays
funcion=np.array(funcion)
tiempo=np.array(tiempo)
normal=periodo/(N)
T_fourier=np.fft.fft(funcion)*normal
freq_T_fourier=np.fft.fftfreq(funcion.size)


#Intento de la funcion obtenida manualmente
############################
#Fallida
x=np.linspace(-5,5,10000)
w=np.fft.fftfreq(x.size)
funcion_w=(-A/(4*w**2))*(4*np.exp(1j*w)+np.exp(-4j*w)-5)
ifft=np.fft.ifft(funcion_w)
###################

#graficos
plt.figure(2)
plt.plot(tiempo,funcion)
plt.title("Señal original")
plt.xlabel("t")
plt.ylabel("f(t)")
plt.figure(3)
plt.plot(freq_T_fourier,abs(T_fourier),color='red')
plt.title("Transformada original")
plt.xlabel("w")
plt.ylabel("|F(w)|")
plt.figure(4)
plt.plot(w,funcion_w,color='blue')
plt.title("Transformada obtenida mediante la funcion calculada a mano")
plt.xlabel("w")
plt.ylabel("|F(w)|")
plt.figure(5)
plt.plot(x,ifft,color='blue')
plt.title("Señal obtenida desde la antitransformada")
plt.xlabel("t")
plt.ylabel("f(t)")


plt.show()

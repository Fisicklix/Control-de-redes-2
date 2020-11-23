import numpy as np
import matplotlib.pyplot as plt
#se define el periodo a utilizar
periodo=10
i=0
#el intervalo es simetrico
intervalo=5
#una lista para las funciones y el tiempo
funcion_triangular=[]
funcion_cuadrada=[]
tiempo=[]
#desde donde se reccore
t=-intervalo
#se forman las funciones
while(t<intervalo):
	tiempo.append(t)
	if(t>=-1 and t<=1):
		funcion_cuadrada.append(1)
	else:
		funcion_cuadrada.append(0)
	if(t>=0 and t<=3):
		funcion_triangular.append(t/3)
	else:
		funcion_triangular.append(0)
	
	t+=1/1000
#El tamaño de los vectores
N=len(tiempo)
#convertidos a arrays
funcion_cuadrada=np.array(funcion_cuadrada)
funcion_triangular=np.array(funcion_triangular)
tiempo=np.array(tiempo)

#la normalizacion de las señales, dado que con el metodo empleado en por convolve realiza la suma, y mientras mas datos se tengan mas grande sera esta
normal=periodo/(N)
convolucion=np.convolve(funcion_triangular,funcion_cuadrada,mode='same')*normal

T_fourier_cuadrada=np.fft.fft(funcion_cuadrada)*normal
T_fourier_triangular=np.fft.fft(funcion_triangular)*normal
T_fourier_convolucion=np.fft.fft(convolucion)*normal


#se realiza la multiplicacion de las transformadas
multiplicacion_T_fourier=T_fourier_triangular*T_fourier_cuadrada
#calcuo de las frec
freq_T_fourier_convolucion=np.fft.fftfreq(convolucion.size)
freq_T_fourier_cuadrada=np.fft.fftfreq(funcion_cuadrada.size,d=1/periodo)
freq_T_fourier_triangular=np.fft.fftfreq(funcion_triangular.size,d=1/periodo)
freq_T_fourier_mult=np.fft.fftfreq(multiplicacion_T_fourier.size,d=1/periodo)
#se vuelve a la señal original desde la multiplicaionde las transformadas
ifft_fourier=np.fft.ifft(multiplicacion_T_fourier)/normal



#Graficos
plt.figure(1)
plt.plot(tiempo,funcion_cuadrada,color='red')
plt.plot(tiempo,funcion_triangular,color='blue')
plt.title("Grafico de señales originales")
plt.ylabel("f(t)")
plt.xlabel("t")

plt.figure(2)
plt.plot(tiempo,convolucion)
plt.title("Grafico de la convolucion de señales originales")
plt.ylabel("f(t)")
plt.xlabel("t")

plt.figure(3)
plt.plot(freq_T_fourier_triangular,abs(T_fourier_cuadrada),color='red')
plt.title("Grafico de la transformada de la funcion triangular")
plt.ylabel("|F(w)|")
plt.xlabel("w")

plt.figure(4)
plt.plot(freq_T_fourier_cuadrada,abs(T_fourier_cuadrada),color='blue')
plt.title("Grafico de la transformada de la funcion cuadrada")
plt.ylabel("|F(w)|")
plt.xlabel("w")
plt.figure(5)
plt.plot(freq_T_fourier_convolucion,abs(T_fourier_convolucion),color='green')
plt.title("Grafico de la transformada de la convolucion")
plt.ylabel("|F(w)|")
plt.xlabel("w")

plt.figure(6)
plt.plot(freq_T_fourier_mult,abs(multiplicacion_T_fourier),color='green')
plt.title("Grafico de la multiplicación de las transformadas")
plt.ylabel("|F(w)|")
plt.xlabel("w")

print(np.sum(abs(multiplicacion_T_fourier)-abs(T_fourier_convolucion)))
plt.show()

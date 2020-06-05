from scipy import signal
import numpy as np
import matplotlib.pyplot as plt


N = 1024

#text_file = np.loadtxt(fname = "noise.txt", dtype = float)

rand_sample = np.random.uniform(0,1,N)


ft = np.fft.fft(rand_sample)
k = np.fft.fftfreq(N, d=1)
order = np.argsort(k)
k = k[order]
k = 2*np.pi*k
aft =  abs(ft[order])
##################################################################
fig = plt.figure()
plt.plot(rand_sample, "g.", label = "rand_sampple")
plt.grid(True)
plt.xlabel('index')
plt.ylabel('sampple_data')
plt.legend()
plt.show()

spectra=aft*aft/(N)

################ "PLoting the power spectrum" ###############################################
fig = plt.figure()
plt.plot(k,spectra, "r-",label='Spectra')
plt.xlabel('frequency')
plt.ylabel('Power spectrum')
plt.legend()
plt.show()



################ "PLoting the Histogram"###############################################


kmax = max(k)
kmin = min(k)


print("Minimum value of k is: ", kmin)
print("Maximum value of k is: ", kmax)
bins=5
k_width=int(kmax-kmin)/bins
K1=np.linspace(kmin,kmax,bins+1)

Power_bin=np.zeros(bins) ##binned power spectram 
K_bin=np.zeros(bins) ## avg value of k in bin
for i in range(bins):
	p = 0
	for j in range(len(k)):
		if K1[i]<=k[j]<K1[i+1]:
			Power_bin[i]+=spectra[j]
			p = p+1
	Power_bin[i]=Power_bin[i]/p	
	K_bin[i]=K1[i]+(K1[i+1]-K1[i])/2
fig1,ax1=plt.subplots()
ax1.bar(K_bin,Power_bin,k_width)
ax1.set_xlabel("Binned K")
ax1.set_ylabel("Binned power spectra")
ax1.set_title("Histogram for binned power spectrum")
plt.show()
















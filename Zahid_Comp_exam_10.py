import numpy as np
import matplotlib.pyplot as plt

def f(x):
    if (-1.0<x<1.0):
        return 1
    else:
        return 0    
xmin = -5.0
xmax = 5.0

n = 2 ** (7)

dx = (xmax - xmin) / (n - 1)
#print(dx)

sampled_data = np.zeros(n)
x = np.zeros(n)

for i in range(n):
    sampled_data[i] = f(xmin + i * dx)
    x[i] = xmin + i * dx
# print(sampled_data)
#print("x=", x)
# nft = (np.fft.fft(sampled_data, norm = 'ortho'))
# print(nft)

k = np.fft.fftfreq(n, dx)

# print('k=',k)
I = np.argsort(k)
k = k[I]
#print("k=", k)
k = 2 * np.pi * k
# print("k_new=", k)

nft = (np.fft.fft(sampled_data, norm='ortho'))
nft = nft[I]

factor = np.exp(-1j * k * xmin)
# print("factor=", factor)


ft = (abs((dx * np.sqrt(n / (2 * np.pi)) * factor * nft)))
plt.figure()
plt.plot(k, ft, "red", label= "NFT")
plt.xlabel("Frequency")
plt.ylabel("Fourier transform")
plt.grid()
plt.title("Fourier tansform for n=128")
plt.legend()
plt.figure()
plt.plot(x, sampled_data)
plt.xlabel("x")
plt.ylabel("Sampled_data")
plt.title("Graph of Sampled data for n=128")
plt.legend()
plt.show()

#################################################################################

n = 2 ** (6)

dx = (xmax - xmin) / (n - 1)
#print(dx)

sampled_data = np.zeros(n)
x = np.zeros(n)

for i in range(n):
    sampled_data[i] = f(xmin + i * dx)
    x[i] = xmin + i * dx
# print(sampled_data)
#print("x=", x)
# nft = (np.fft.fft(sampled_data, norm = 'ortho'))
# print(nft)

k = np.fft.fftfreq(n, dx)

# print('k=',k)
I = np.argsort(k)
k = k[I]
#print("k=", k)
k = 2 * np.pi * k
# print("k_new=", k)

nft = (np.fft.fft(sampled_data, norm='ortho'))
nft = nft[I]

factor = np.exp(-1j * k * xmin)
# print("factor=", factor)


ft = (abs((dx * np.sqrt(n / (2 * np.pi)) * factor * nft)))
plt.figure()
plt.plot(k, ft, "red", label= "NFT")
plt.xlabel("Frequency")
plt.ylabel("Fourier transform")
plt.grid()
plt.title("Fourier tansform for n=64")
plt.legend()
plt.figure()
plt.plot(x, sampled_data)
plt.xlabel("x")
plt.ylabel("Sampled_data")
plt.title("Graph of Sampled data for n=64")
plt.legend()
plt.show()

#########################################################


n = 2 ** (5)

dx = (xmax - xmin) / (n - 1)
#print(dx)

sampled_data = np.zeros(n)
x = np.zeros(n)

for i in range(n):
    sampled_data[i] = f(xmin + i * dx)
    x[i] = xmin + i * dx
# print(sampled_data)
#print("x=", x)
# nft = (np.fft.fft(sampled_data, norm = 'ortho'))
# print(nft)

k = np.fft.fftfreq(n, dx)

# print('k=',k)
I = np.argsort(k)
k = k[I]
#print("k=", k)
k = 2 * np.pi * k
# print("k_new=", k)

nft = (np.fft.fft(sampled_data, norm='ortho'))
nft = nft[I]

factor = np.exp(-1j * k * xmin)
# print("factor=", factor)


ft = (abs((dx * np.sqrt(n / (2 * np.pi)) * factor * nft)))
plt.figure()
plt.plot(k, ft, "red", label= "NFT")
plt.xlabel("Frequency")
plt.ylabel("Fourier transform")
plt.grid()
plt.title("Fourier tansform for n=32")
plt.legend()
plt.figure()
plt.plot(x, sampled_data)
plt.xlabel("x")
plt.ylabel("Sampled_data")
plt.title("Graph of Sampled data for n=32")
plt.legend()
plt.show()




###########################################################

















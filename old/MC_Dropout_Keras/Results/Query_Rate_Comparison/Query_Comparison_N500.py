# http://www.scipy-lectures.org/intro/matplotlib/matplotlib.html
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from matplotlib import rc, rcParams
import matplotlib.dates as dates
import pylab as pl

  # activate latex text rendering
rc('text', usetex=True)
rc('axes', linewidth=2)
rc('font', weight='bold')
rcParams['text.latex.preamble'] = [r'\usepackage{sfmath} \boldmath']

Bald_Q1 = np.load('Bald_Q1.npy')
Dropout_ME_Q1 = np.load('Dropout_ME_Q1.npy')
Segnet_Q1 = np.load('Segnet_Q1_N1000.npy')
VarRatio_Q1 = np.load('VarRatio_Q1_N1000.npy')


Bald_Q5 = np.load('Bald_Q5.npy')
Dropout_ME_Q5 = np.load('Dropout_ME_Q5.npy')
Segnet_Q5 = np.load('Segnet_Q5.npy')
VarRatio_Q5 = np.load('VarRatio_Q5.npy')

Bald_Q10 = np.load('Bald_Q10.npy')
Dropout_ME_Q10 = np.load('Dropout_ME_Q10.npy')
Segnet_Q10 = np.load('Segnet_Q10.npy')
VarRatio_Q10 = np.load('VarRatio_Q10.npy')

Bald_Q100 = np.load('Bald_Q100.npy')
Dropout_ME_Q100 = np.load('Dropout_ME_Q100.npy')
Segnet_Q100 = np.load('Segnet_Q100.npy')
VarRatio_Q100 = np.load('VarRatio_Q100.npy')





Q1 = np.arange(100, 501, 1)
Q5 = np.arange(100, 505, 5)
Q10 = np.arange(100, 510, 10)
Q100 = np.arange(100, 600, 100)


plt.figure(figsize=(15, 10), dpi=80)

pl.subplot(2, 2, 1) 
plt.plot(Q1, Bald_Q1[0:401], color="green", linewidth=1.0, label=r"\textbf{Queries = 1 per acquisition}" )
plt.plot(Q5, Bald_Q5[0:81], color="red", linewidth=1.0, marker='.', label=r"\textbf{Queries = 5 per acquisition}" )
plt.plot(Q10, Bald_Q10[0:41], color="black", linewidth=1.0, marker='.', label=r"\textbf{Queries = 10 per acquisition}" )
plt.plot(Q100, Bald_Q100[0:5], color="blue", linewidth=1.0, marker='.', label=r"\textbf{Queries = 100 per acquisition}" )
plt.title(r'\textbf{Dropout BALD}')
plt.xlabel('Number of Labelled Sampples')
plt.ylabel('Test Accuracy')
plt.grid()
plt.legend(loc = 4)


pl.subplot(2, 2, 2)
plt.plot(Q1, Dropout_ME_Q1[0:401], color="green", linewidth=1.0, label=r"\textbf{Queries = 1 per acquisition}" )
plt.plot(Q5, Dropout_ME_Q5[0:81], color="red", linewidth=1.0, marker='.', label=r"\textbf{Queries = 5 per acquisition}" )
plt.plot(Q10, Dropout_ME_Q10[0:41], color="black", linewidth=1.0, marker='.', label=r"\textbf{Queries = 10 per acquisition}" )
plt.plot(Q100, Dropout_ME_Q100[0:5], color="blue", linewidth=1.0, marker='.', label=r"\textbf{Queries = 100 per acquisition}" )
plt.title(r'\textbf{Dropout Maximum Entropy}')
plt.xlabel('Number of Labelled Sampples')
plt.ylabel('Test Accuracy')
plt.grid()
plt.legend(loc = 4)

pl.subplot(2, 2, 3)
plt.plot(Q1, Segnet_Q1[0:401], color="green", linewidth=1.0, label=r"\textbf{Queries = 1 per acquisition}" )
plt.plot(Q5, Segnet_Q5[0:81], color="red", linewidth=1.0, marker='.', label=r"\textbf{Queries = 5 per acquisition}" )
plt.plot(Q10, Segnet_Q10[0:41], color="black", linewidth=1.0, marker='.', label=r"\textbf{Queries = 10 per acquisition}" )
plt.plot(Q100, Segnet_Q100[0:5], color="blue", linewidth=1.0, marker='.', label=r"\textbf{Queries = 100 per acquisition}" )
plt.title(r'\textbf{Dropout Bayes Segnet}')
plt.xlabel('Number of Labelled Sampples')
plt.ylabel('Test Accuracy')
plt.grid()
plt.legend(loc = 4)

pl.subplot(2, 2, 4)
plt.plot(Q1, VarRatio_Q1[0:401], color="green", linewidth=1.0, label=r"\textbf{Queries = 1 per acquisition}" )
plt.plot(Q5, VarRatio_Q5[0:81], color="red", linewidth=1.0, marker='.', label=r"\textbf{Queries = 5 per acquisition}" )
plt.plot(Q10, VarRatio_Q10[0:41], color="black", linewidth=1.0, marker='.', label=r"\textbf{Queries = 10 per acquisition}" )
plt.plot(Q100, VarRatio_Q100[0:5], color="blue", linewidth=1.0, marker='.', label=r"\textbf{Queries = 100 per acquisition}" )
plt.title(r'\textbf{Dropout Variation Ratio}')
plt.xlabel('Number of Labelled Sampples')
plt.ylabel('Test Accuracy')
plt.grid()
plt.legend(loc = 4)



plt.show()

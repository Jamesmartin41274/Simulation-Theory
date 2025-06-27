import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import logistic

#Starting with the introduction of our 10000000 samples from the uniform distribution u ~ U(0,1)
u = np.random.uniform(0,1,10000000)

#Inversion of the CDF:
x = -np.log(1/u -1)

# Drawing the Histogram plot
plt.hist(x, bins=100,density=True,alpha=0.5,label = "Sampled Data" )

# Plotting the logistic pdf with the mean  = 0 and scale = 1
x_vals = np.linspace(-10,10,10000)
pdf_values = logistic.pdf(x_vals,loc = 0,scale =1)

plt.plot(x_vals,pdf_values,'r-', lw=2, label='True PDF (Logistic(0,1))')

plt.title('Inverse CDF Sampling from Logistic(0,1)')
plt.xlabel('x')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
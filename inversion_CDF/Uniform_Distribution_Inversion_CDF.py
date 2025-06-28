import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform

# Creating a sample of uniform random variables u ~ U(0,1)
u= np.random.uniform(0,1,10000000)

#Imversion CDF of X ~U(2,5)
x = 3*u+2 

#Plotting the Histogram of the updated sample 
plt.hist(x,bins = 50, density =True, alpha = 0.5, label ="Histogram Plot of the Inversion CDF")

x_vals = np.linspace(2,5,1000)
pdf_vals = uniform.pdf(x_vals, loc=2, scale=3)  # Uniform(2,5) has scale = 5-2 = 3

plt.plot(x_vals, pdf_vals, 'r-', lw=2, label='True PDF (Uniform(2,5))')

plt.title('Inverse CDF Sampling from Uniform(2,5)')
plt.xlabel('x')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
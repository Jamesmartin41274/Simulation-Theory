import numpy as np
import matplotlib.pyplot as plt
#sample sizes 
sample_size=np.array([10,100,1000,10000,100000,10000000])
catastrophe_probabilities = []
for n in sample_size:
    x_numbers = np.random.uniform(-1,1,n)
    y_numbers = np.random.uniform(-1,1,n)
    # Catastrophic region checker x^2+y^2 <=1
    x_square_numbers = np.square(x_numbers)
    y_square_numbers = np.square(y_numbers)
    z_square_numbers = x_square_numbers+y_square_numbers
    danger_zone = z_square_numbers<=0.3
    safe_zone =z_square_numbers>0.3
    catasrophic_outcomes= np.sum(danger_zone)
    #probability of catastrophe
    catasrophe_probability = catasrophic_outcomes/n
    catastrophe_probabilities.append(catasrophe_probability)
print(catastrophe_probabilities)


plt.plot(sample_size,catastrophe_probabilities)
plt.xlabel("sample size")
plt.ylabel("catstrophe probaility")
plt.title("Basic Monte Carlo on catstrophe probability")
plt.xscale("log")
plt.show()
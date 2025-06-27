import numpy as np
import matplotlib.pyplot as plt
# 2 dimensional sample
x_numbers = np.random.uniform(-1,1,1000)
y_numbers = np.random.uniform(-1,1,1000)

# Catastrophic region checker x^2+y^2 <=1
x_square_numbers = np.square(x_numbers)
y_square_numbers = np.square(y_numbers)
z_square_numbers = x_square_numbers+y_square_numbers

danger_zone = z_square_numbers<=0.3
3
catasrophic_outcomes= np.sum(danger_zone)
sample_size =len(x_numbers)

#probability of catastrophe
catasrophe_probability = catasrophic_outcomes/sample_size
print(catasrophe_probability)


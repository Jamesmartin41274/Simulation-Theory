import numpy as np

# Step 1: Generate 1000 uniform numbers between 0 and 1
numbers = np.random.uniform(0, 1, 1000)

# Step 2: Apply inverse CDF transformation: X = sqrt(U)
transformed = np.sqrt(numbers)

# Step 3: Count how many values are in the danger zone: x > 0.8
danger_zone = transformed > 0.8
number_of_catastrophic_outcomes = np.sum(danger_zone)

# Step 4: Estimate probability of catastrophe
n = len(numbers)
probability_of_catastrophe = number_of_catastrophic_outcomes / n

# Step 5: Print result
print("Probability of catastrophe is:", probability_of_catastrophe)
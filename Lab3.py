import random
import matplotlib.pyplot as plt

# Function to generate N random points and count how many fall inside the circle
def estimate_pi(N):
    count = 0
    for i in range(N):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            count += 1
    return 4 * count / N

# List of sample sizes to use
Ns = [10**k for k in range(1, 8)]

# Loop over sample sizes and average the result 100 times for each size
errors = []
for N in Ns:
    total_error = 0
    for _ in range(100):
        estimated_pi = estimate_pi(N)
        total_error += abs(estimated_pi - 3.141592653589793)
    errors.append(total_error / 100)

# Plot the results in double-logarithmic scale
plt.loglog(Ns, errors)
plt.xlabel('N')
plt.ylabel('|π - π\'|')
plt.title('Absolute error in estimating π using Monte Carlo simulation')
plt.show()


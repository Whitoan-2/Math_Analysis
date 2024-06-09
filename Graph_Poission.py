import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Set the parameter for the Poisson distribution
lambda_param = 4  # The average rate (λ) of the Poisson distribution

# Generate the range of x values
x = np.arange(0, 10)  # Adjust the range as needed to show more or fewer values

# Calculate the Poisson PMF values for each x
pmf_values1 = poisson.pmf(x, lambda_param)
pmf_values2 = poisson.pmf(x, 5)
pmf_values3 = poisson.pmf(x, 4.5)
pmf_values4 = poisson.pmf(x, 5.5)
# Create the histogram
fig, ax = plt.subplots(2,2)
ticks = [0,1,2,3,4,5,6,7,8,9,10]

ax[0][0].set_xticks(ticks)
ax[0][1].set_xticks(ticks)
ax[1][0].set_xticks(ticks)
ax[1][1].set_xticks(ticks)

ax[0][0].bar(x, pmf_values1, width=1.0, edgecolor='black', color='lightblue', alpha = 0.25, label = "Distribution")  # No fill color initially
ax[0][1].bar(x, pmf_values2, width=1.0, edgecolor='black', color='lightblue', alpha = 0.25)  # No fill color initially
ax[1][0].bar(x, pmf_values3, width=1.0, edgecolor='black', color='lightblue', alpha = 0.25)  # No fill color initially
ax[1][1].bar(x, pmf_values4, width=1.0, edgecolor='black', color='lightblue', alpha = 0.25)  # No fill color initially
ax[0][0].set_title("λ = 4")
ax[0][1].set_title("λ = 5")
ax[1][0].set_title("λ = 4.5")
ax[1][1].set_title("λ = 5.5")
ax[0][0].axvline(3.5,color = "crimson", label = "Expected Maximum")
ax[0][1].axvline(4.5,color = "crimson")
ax[1][0].axvline(4,color = "crimson")
ax[1][1].axvline(5,color = "crimson")
fig.legend()
# Show the plot
plt.show()
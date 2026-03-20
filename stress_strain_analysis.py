import numpy as np
import matplotlib.pyplot as plt

# Sample strain data
strain = np.array([0.000, 0.002, 0.004, 0.006, 0.008, 0.010])

# Sample stress data (MPa)
stress = np.array([0, 150, 300, 450, 550, 600])

# Plot graph
plt.plot(strain, stress, marker='o')
plt.xlabel("Strain")
plt.ylabel("Stress (MPa)")
plt.title("Stress-Strain Curve")
plt.grid()

# Highlight linear region
plt.plot(strain[:3], stress[:3], color='green', label='Elastic Region')
plt.legend()

plt.show()

# Calculate Young's Modulus (slope of linear region)
youngs_modulus = (stress[2] - stress[0]) / (strain[2] - strain[0])
print(f"Young's Modulus: {youngs_modulus:.2f} MPa")
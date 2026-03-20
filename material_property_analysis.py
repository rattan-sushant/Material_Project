import numpy as np
import matplotlib.pyplot as plt
# Material names
materials = ["Steel", "Aluminum", "Copper"]
# Density (kg/m^3)
density = np.array([7850, 2700, 8960])
# Strength (MPa)
strength = np.array([400, 300, 220])

# Plot scatter graph
plt.scatter(density, strength)

# Label each point
for i in range(len(materials)):
    plt.text(density[i], strength[i], materials[i])

plt.xlabel("Density (kg/m^3)")
plt.ylabel("Strength (MPa)")
plt.title("Material Comparison: Strength vs Density")
plt.grid()

# Sort by density
sorted_indices = np.argsort(density)
density_sorted = density[sorted_indices]
strength_sorted = strength[sorted_indices]

# Plot sorted line
plt.plot(density_sorted, strength_sorted, linestyle='--', color='gray')

# plt.plot(density, strength, linestyle='--')

plt.show()
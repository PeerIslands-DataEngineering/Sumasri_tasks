import numpy as np

resources = np.array([
    [15, 40, 32],
    [20, 42, 35],
    [25, 38, 30],
    [18, 50, 40],
    [22, 37, 36],
    [28, 45, 33]
])

total_per_resource = np.sum(resources, axis=0)
print(f"Total resources needed (tons): Oxygen: {total_per_resource[0]}, Water: {total_per_resource[1]}, Food: {total_per_resource[2]}")

max_values = np.max(resources, axis=0)
oxygen_max, water_max, food_max = max_values

month_water = np.argmax(resources[:, 1]) 
print(f"Highest consumption in a month: Water ({water_max} tons in month {month_water})")

std_dev = np.std(resources, axis=0)
print(f"Standard deviation of consumption: Oxygen: {std_dev[0]:.1f}, Water: {std_dev[1]:.1f}, Food: {std_dev[2]:.1f}")

transposed = resources.T
print("\nTransposed matrix:")
for row in transposed:
    print(row)
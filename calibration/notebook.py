import matplotlib.pyplot as plt
import numpy as np

# Importing Data

# assign empty list for x value and y value
x = []
y = []

# open file in read mode
with open('20251105 Na-22 01.csv', 'r', newline='') as file:
    # skip header
    next(file)

    for line in file:
        # split column
        line_splitted = line.split(',')

        # convert data to float and append
        x.append(float(line_splitted[0]))
        y.append(float(line_splitted[1]))

# Masking everything but the highest peak

# convert lists to numpy arrays
x_array = np.array(x)
y_array = np.array(y)

# define x range to mask
x_min, x_max = 1822, 2336

# create mask
mask = (x_array < x_min) | (x_array > x_max)

# masked and non-masked data
x_masked = x_array[mask]
y_masked = y_array[mask]

x_selection = x_array[~mask]
y_selection = y_array[~mask]

# create new figure
plt.figure()

# scatter plot
plt.scatter(x_selection, y_selection)        # non-masked points (default color)
plt.scatter(x_masked, y_masked, color='r')   # masked points (red)

plt.xlabel("Voltage (mV)")
plt.ylabel("Counts")
plt.title("Masked data between 1822 and 2336")
plt.show()

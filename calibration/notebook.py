import matplotlib.pyplot as plt
import numpy as np
from lmfit import models



# %% Opening File

# Importing Data
x = []
y = []

# open file in read mode
with open('20251105 Na-22 01.csv', 'r', newline='') as file:
    # skip header
    next(file)

    for line in file:
        # split column
        line_splitted = line.split(',')
        x.append(float(line_splitted[0]))
        y.append(float(line_splitted[1]))

# Convert lists to numpy arrays
x_array = np.array(x)
y_array = np.array(y)


# %% Define ranges of masked / unmasked ranges

# Define the two unmasked x-ranges
x_min1, x_max1 = 60, 1240
x_min2, x_max2 = 1822, 2336

# Create boolean masks for each unmasked range
mask_range1 = (x_array >= x_min1) & (x_array <= x_max1)
mask_range2 = (x_array >= x_min2) & (x_array <= x_max2)

# Combine both unmasked ranges
unmasked_mask = mask_range1 | mask_range2

# Masked = everything outside both ranges
masked_mask = ~unmasked_mask

# Separate data for plotting/fitting
x_selection_1 = x_array[mask_range1]
y_selection_1 = y_array[mask_range1]

x_selection_2 = x_array[mask_range2]
y_selection_2 = y_array[mask_range2]

x_masked = x_array[masked_mask]
y_masked = y_array[masked_mask]


# %% Fit to Gaussian funtion

# --- Fit Gaussian to first range ---
gauss1 = models.GaussianModel(prefix='g1_')
pars1 = gauss1.guess(y_selection_1, x=x_selection_1)
result1 = gauss1.fit(y_selection_1, pars1, x=x_selection_1)

# --- Fit Gaussian to second range ---
gauss2 = models.GaussianModel(prefix='g2_')
pars2 = gauss2.guess(y_selection_2, x=x_selection_2)
result2 = gauss2.fit(y_selection_2, pars2, x=x_selection_2)


# %% Creating Plot with Gaussian fits

plt.figure(figsize=(10, 6))

# masked data (outside both peaks)
plt.scatter(x_masked, y_masked, color='r', label='Masked data')

# unmasked and fitted data for each peak
plt.scatter(x_selection_1, y_selection_1, label='1st peak (data)')
plt.plot(x_selection_1, result1.best_fit, 'k--', label='1st peak (Gaussian fit)')

plt.scatter(x_selection_2, y_selection_2, label='2nd peak (data)')
plt.plot(x_selection_2, result2.best_fit, 'b--', label='2nd peak (Gaussian fit)')

plt.xlabel("Voltage (mV)")
plt.ylabel("Counts")
plt.title("Gaussian Fits for Peaks at 60–1240 mV and 1822–2336 mV")
plt.legend()
plt.show()


# %% Printing fit result

print("\n=== Gaussian Fit 1 (60–1240 mV) ===")
print(result1.fit_report())

print("\n=== Gaussian Fit 2 (1822–2336 mV) ===")
print(result2.fit_report())


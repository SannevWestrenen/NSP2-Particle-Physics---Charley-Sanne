# assign empty list for x value and y value
x = []
y = []

# open file in read mode
with open('20251105 Na-22 01.csv', 'r', newline='') as file:

    # to skip header:
    # read and discard first line of file
    next(file)

    for line in file:
        # split column
        line_splitted = line.split(',')

        # convert data to float
        # append data to list
        x.append(float(line_splitted[0]))
        y.append(float(line_splitted[1]))

print(x, y)
import matplotlib.pyplot

data = []
associativity_size = {1: [], 2: [], 4: [], 8: []}

with open("C:\\Users\\shubh\\Downloads\\CA\\Assignment 1\\Graph & Output\\miss_rate.txt", "r") as file:
    for line in file:
        parts = line.split()
        data.append((parts[0], int(parts[1]), float(parts[2])))

for size, associativity, miss_rate in data:
    associativity_size[associativity].append((size, miss_rate))

for associativity, values in associativity_size.items():
    sizes, miss_rate = zip(*values)
    matplotlib.pyplot.plot(sizes, miss_rate, marker = ".", label = f'{associativity}-way')

matplotlib.pyplot.legend()
matplotlib.pyplot.xlabel('Cache Size (KB)')
matplotlib.pyplot.ylabel('Miss Rate Per Type')
matplotlib.pyplot.title ('Miss Rate Per Type vs Cache Size (KB)')
matplotlib.pyplot.show()
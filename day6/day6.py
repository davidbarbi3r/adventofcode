data_stream = []

with open("./test.txt") as file:
    lines = file.readlines()
    data_stream = [row.strip() for row in lines]

print(data_stream)

for stream in data_stream:
    for i in range(len(stream)):
        if len(stream[i:i+14]) == len(set(stream[i:i+14])):
            print(f"solution 2: {i+14}")
            break

for stream in data_stream:
    for i in range(len(stream)):
        if len(stream[i:i+4]) == len(set(stream[i:i+4])):
            print(f"solution 1: {i+4}")
            break
stack = []
commands = []

with open("./stack.txt") as file:
    lines = file.readlines()
    stack = [row.strip() for row in lines]
    for line in stack:
        line.split("")

with open("./day5.txt") as file:
    lines = file.readlines()
    commands = [row.strip() for row in lines]

stack[0] = stack[0].replace('\ufeff', '')

for command in commands:
    command = command.split(" ")
    for i in range(int(command[1])):
        stack[int(command[5])-1]+=(stack[int(command[3])].pop(-1))

print(stack)
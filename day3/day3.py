

all_bags = []
equals = []
results = []
groups = []
badges = []
badges_priority = []

with open("./input.txt") as file:
    lines = file.readlines()
    all_bags = [row.strip() for row in lines]


# part 1

for bag in all_bags: 
    middle = len(bag)//2
    part1 = bag[:middle]
    part2 = bag[middle:]

    for item2 in part2:
        duplicate = '' 

        for item1 in part1:

            if item2 == item1: 
                duplicate = item2
                break
        if duplicate: 
            equals.append(duplicate)
            break

for duplicate in equals:
        if ord(duplicate) > 96: 
            results.append(ord(duplicate)-96)
        else: 
            results.append(ord(duplicate)-64+26)

print(f"solution 1: {sum(results)}")


# part 2

for i in range(0, len(all_bags), 3):
    groups.append(all_bags[i: i+3])

for group in groups:
    badges.extend(set.intersection(*[set(elve) for elve in group]))

for badge in badges:
    if ord(badge) > 96: 
        badges_priority.append(ord(badge)-96)
    else: 
        badges_priority.append(ord(badge)-64+26)


print(f"solution 2: {sum(badges_priority)}")

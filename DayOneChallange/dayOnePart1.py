left_list = []
right_list = []

with open('input.txt', 'r') as file:
    for line in file:
        right, left = map(int, line.strip().split())
        left_list.append(left)
        right_list.append(right)

left_list.sort()
right_list.sort()
total_distance = 0

for i in range(0, len(left_list)):
    total_distance += abs(left_list[i] - right_list[i])

print(total_distance)
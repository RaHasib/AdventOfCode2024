from collections import defaultdict, deque


def read_input_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    rules_part, updates_part = content.strip().split('\n\n')
    rules = rules_part.splitlines()
    updates = [list(map(int, line.split(','))) for line in updates_part.splitlines()]

    return rules, updates


def is_correctly_ordered(update, rules):
    for rule in rules:
        x, y = map(int, rule.split('|'))
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True


def correct_order(update, rules):
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    update_set = set(update)
    for rule in rules:
        x, y = map(int, rule.split('|'))
        if x in update_set and y in update_set:
            graph[x].append(y)
            in_degree[y] += 1

    # Topological sort using Kahn's algorithm
    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_update = []

    while queue:
        node = queue.popleft()
        sorted_update.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_update


def calculate_middle_page_sum_for_incorrect_updates(file_path):
    rules, updates = read_input_file(file_path)
    middle_pages_sum = 0

    for update in updates:
        if not is_correctly_ordered(update, rules):
            corrected_update = correct_order(update, rules)
            middle_index = len(corrected_update) // 2
            middle_pages_sum += corrected_update[middle_index]

    return middle_pages_sum


file_path = 'input.txt'
result = calculate_middle_page_sum_for_incorrect_updates(file_path)
print(f"Sum of middle page numbers after correcting incorrect updates: {result}")

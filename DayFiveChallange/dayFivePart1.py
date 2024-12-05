def read_input_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Splitting the content into rules and updates sections
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


def calculate_middle_page_sum(file_path):
    rules, updates = read_input_file(file_path)
    middle_pages_sum = 0

    for update in updates:
        if is_correctly_ordered(update, rules):
            middle_index = len(update) // 2
            middle_pages_sum += update[middle_index]

    return middle_pages_sum


file_path = 'input.txt'
result = calculate_middle_page_sum(file_path)
print(f"Sum of middle page numbers: {result}")

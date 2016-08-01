def integer_operations(initial_value):
    items = []
    for count in range(0, 6):
        items.append(initial_value)
        initial_value += 1
    return sum(items)


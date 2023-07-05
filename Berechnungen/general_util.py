def print_table(data):
    formatted_row = "{:<6}" * len(data)
    print(formatted_row.format(*data))
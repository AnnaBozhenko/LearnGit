def decreasing(list_input, list_output = []):
    if list_input == []:
        return list_output
    maximum = max(list_input)
    # Remove all the numbers which equal to muximum in the input_list.
    amount = list_input.count(maximum)
    for i in range(amount):
        list_input.remove(maximum)
        list_output.append(maximum)
    return decreasing(list_input, list_output)
    
def increasing(list_input, list_output = []):
    if list_input == []:
        return list_output
    minimum = min(list_input)
    # Remove all the numbers which equal to minimum in the input_list.
    amount = list_input.count(minimum)
    for i in range(amount):
        list_input.remove(minimum)
        list_output.append(minimum)
    return increasing(list_input, list_output)

list_data = [(1, 1), (2, -3), (6, 4), (4, 8)]

def decreasing_list(list_input):
    maxim = list_data[0][-1]
    def inner(list_input, maxim, list_output = [], index = 0):
        if list_input == []:
            return list_output
        number = list_input[index[-1]]
        if number >= maxim():
            maxim = number
            list_output.append(list_input[index])
            list_data.pop(index)
            return inner(list_data, maxim, list_output, index)
    return inner(list_input, maxim, list_output = [], index = 0)

print(decreasing_list(list_data))
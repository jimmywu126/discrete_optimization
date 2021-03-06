import time


def calculate_total_value(item_selected, values):
    """
    Given lists of item values and items selected, returns the achieved objective value.
    """
    return sum(values[i] * item_selected[i] for i in xrange(len(values)))

def calculate_total_weight(item_selected, weights):
    """
    Given lists of item values and items selected, returns the total weight used.
    """
    return sum(weights[i] * item_selected[i] for i in xrange(len(weights)))



def parse_input(input_data):
    """
    Given a string of data from an input file, returns:
        - Capacity of knapsack
        - List of item values
        - List of item weights
    """
    lines = input_data.split('\n')

    first_line = lines[0].split()
    number_of_items = int(first_line[0])
    capacity = int(first_line[1])
    values, weights = [], []

    for i in xrange(1, number_of_items + 1):
        line = lines[i]
        parts = line.split()

        values.append(int(parts[0]))
        weights.append(int(parts[1]))

    return capacity, values, weights

def generate_output(start_time, end_time, item_selected, capacity=0, values=None, weights=None, is_optimal=0):
    """
    Given a solution, returns a string of the solution formatted per problem specification.
    """
    output_data = str(calculate_total_value(item_selected, values)) + ' ' + str(is_optimal) + '\n'
    output_data += ' '.join(map(str, item_selected))
    return output_data

def generate_custom_output(start_time, end_time, item_selected, capacity, values, weights, is_optimal=0):
    """
    Given a solution, returns a string of the solution along with helpful information.
    Does not conform to the problem specification.
    """
    total_value = calculate_total_value(item_selected, values)
    total_weight = calculate_total_weight(item_selected, weights)

    output_data = 'Total value:\t' + str(total_value) + ' '
    output_data += '(optimal)' if is_optimal == 1 else ' (no optimality proof)'
    output_data += '\nTotal weight:\t' + str(total_weight) + '\t\tCapacity:\t' + str(capacity) + '\t\t(' + str('%.3f' % (float(total_weight) / float(capacity) * 100)) + '% used)'
    output_data += '\nItems selected:\t' + ' '.join(map(str, item_selected))
    output_data += '\nRunning time:\t' + str('%.1f' % (end_time - start_time)) + ' seconds'
    return output_data



import math


def sum(values):
    """
    :param values: a list of values
    :return: the sum of all the values in the list
    """
    for i in range(len(values)):
        sum += values[i]
    return float(sum)


def mean(values):
    """
    :param values: a list of values
    :return: the mean of all the values
    """
    length = len(values)
    mean = 0
    for i in range(length):
        mean += (values[i] / length)

    return float(mean)


def median(values):
    """
    :param values: a list of values
    :return: the median of all the values in the list
    """

    # sort the list of values in order to calculate the median
    values.sort
    length = len(values)

    # check if len is even or odd & calculate the median accordingly
    if length % 2 == 0:
        med = (values[length / 2] + values[length / 2 - 1]) / 2
    else:
        med = values[math. ceil(length / 2) - 1]

    return float(med)


def population_statistics(feature_description, data, treatment, target, threshold, is_above, statistic_functions):
    """
    :param feature_description: a string that describes the name of the group
    :param data: dictionary that contains the data
    :param treatment: a specific feature
    :param target: a specific feature
    :param threshold: threshold to treatment
    :param is_above: a boolean variable
    :param statistic_functions: a list of statistics methods
    :return: void
    """

    # creating a new array based on 'is above' and 'threshold' values
    data1 = []
    for i in range (len(data[target])):
        if is_above == True:
            if data[treatment][i] > threshold:
                data1.append(data[target][i])
        else:
            if data[treatment][i] <= threshold:
                data1.append(data[target][i])

    # executing each function and printing the result
    print_string = feature_description + ": "
    for index, method in enumerate(statistic_functions):
        value = method(data1)
        if index != len(statistic_functions) - 1:
            print_string = print_string + value + ", "
        else:
            print_string = print_string + value

    print(print_string)




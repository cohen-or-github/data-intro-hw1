import pandas


def load_data(path, features):
    """
    :param path: the full path to the selected file
    :param features: the list of features we want to appear in the final dictionary
    :return: the dictionary by the data from the file filtered by the relevant features only
    """
    df = pandas.read_csv(r'C:\Users\tomeriko\Desktop\technion\Python_lab_1\london.csv')
    datatemp = df.to_dict(orient="list")
    # selecting the relevant keys by the features array and filtering the dictionary accordingly
    data = {x: datatemp[x] for x in features}
    return data


def data_with_relevant_indices(list_of_indices, data):
    data_output = {}
    for key in data.keys():
        list_to_pass = []
        for i in list_of_indices:
            list_to_pass.append(data[key][i])
        data_output[key] = list_to_pass
    return data_output


def append_the_elements(i, data_input, data):
    """
    :param i: the relevant column to append the dict
    :param data_input:
    :param data:
    :return: void
    """
    for key in data.keys():
        if not key in data_input:  # if the key doesn't exist, create it
            data_input[key] = []
        data_input[key].append(data[key][i])  # either way, append the element


def filter_by_feature(data, feature, values):
    """
    :param data: dictionary that contains the relevant data
    :param feature: name of a feature which values are categories
    :param values: a set of values that the feature can get
    :return: 2 dictionaries - in the first is all the records in which feature got a value
             from values, and the second is all the records in which it didn't
    """
    data1 = {}
    data2 = {}
    for idx, value in enumerate(data[feature]):
        if value in values:
            append_the_elements(idx, data1, data)
        else:
            append_the_elements(idx, data2, data)
    print(data1)
    return data1, data2

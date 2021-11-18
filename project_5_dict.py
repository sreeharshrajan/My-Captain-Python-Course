string = input('Please enter a string ')


def most_frequent(string):
    # empty dictionary
    d = dict()
    # calculate frequency of all letters
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1

    # sort frquency in decreasing order
    sorted_keys = sorted(d, key=d.get, reverse=True)
    # prints frequency
    for r in sorted_keys:
        print(r, d[r])


most_frequent(string)

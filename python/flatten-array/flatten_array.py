def flatten(nestedList):
    flattenList = []

    for elem in nestedList:
        if isinstance(elem, list):
            flattenList.extend(flatten(elem))
        elif elem is not None:
            flattenList.append(elem)

    return flattenList
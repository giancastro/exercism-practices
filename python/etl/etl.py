def transform(legacy_data):
    newData = {}
    for key, values in legacy_data.items():
        for value in values:
            newData[value.lower()] = key

    return dict(sorted(newData.items()))
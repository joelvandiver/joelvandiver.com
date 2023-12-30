def transform(data):
    '''Transform this data.'''

    return [
        item * idx
        for idx, item in enumerate(data)
    ]


print(transform([1, 2, 3]))
print(transform([['a'], ['b'], ['c']]))


def multiple_by_index(data: list[int]) -> list[int]:
    '''Multiply the numbers by their index.'''

    return [
        num * idx
        for idx, num in enumerate(data)
    ]


print(multiple_by_index([1, 2, 3]))
print(multiple_by_index([['a'], ['b'], ['c']]))
# TODO:  Write a post about inspecting the caller of a function
def sample_func():
    import inspect

    current_frame = inspect.currentframe()
    if current_frame is None:
        print('No current frame')
        return []
    caller_frame = current_frame.f_back
    if caller_frame is None:
        print('No caller frame')
        return []
    caller_code = inspect.getframeinfo(caller_frame).code_context
    if caller_code is None:
        print('No caller code')
        return []
    print("".join(caller_code))

    return []

def main():
    print('Some Before Code')
    print(sample_func([[0, 5], [5, 0]]) == [[0, 5], [5, 0]])
    print('Some After Code')


if __name__ == '__main__':
    main()
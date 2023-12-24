def map_my(func, my_list):
    result = []
    for item in my_list:
        result.append(func(item))
    return result


def main():
    original_list = [1, 2, 3, 4, 5]

    def square(x):
        return x ** 2

    try:
        result_list = map_my(square, original_list)
        print(result_list)
    except Exception as e:
        print(e)


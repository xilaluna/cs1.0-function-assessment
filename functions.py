def area(width, height):
    result = width * height
    return result


def subtract(num1, num2):
    result = num1 - num2
    return result


def divide(num1, num2):
    result = num1 / num2
    return result


def add(num1, num2):
    result = num1 + num2
    return result


area_result = (area(5, 6), area(2, 3))
print(area_result)

sub_result = (subtract(10, 5), subtract(300, 255))
print(sub_result)

add_result = (add(5, 5), add(12, 453))
print(add_result)

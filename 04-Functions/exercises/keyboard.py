def input_string(message):
    value = input(message)
    return str(value)


def input_integer(message):
    value = input(message)
    return int(value)


def input_real(message):
    value = input(message)
    return float(value)


def input_boolean(message):
    value = input(message)
    return value.lower() == "y"

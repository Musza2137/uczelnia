def f(detector):
    people = 0
    for event in detector:
        if event == "+":
            people += 1
            if people >= 3:
                return True
        elif event == "-":
            people -= 1
    return False


print(f("+-+++-+---"))

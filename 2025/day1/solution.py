with open('input.txt', 'r') as file:
    code = [l.strip() for l in file]


def after_rotation(rotations: list) -> int:
    dial = 50
    password = 0
    # 1 to the right at 99 causes it to go to 0
    # 1 to the left at 0 causes it to go to 99
    for rot in rotations:
        if 'R' in rot:
            for _ in range(int(rot[1:])):
                if dial == 99:
                    dial = 0
                else:
                    dial += 1

        elif 'L' in rot:
            for _ in range(int(rot[1:])):
                if dial == 0:
                    dial = 99
                else:
                    dial -= 1
        
        if dial == 0:
            password += 1
    
    return password


def any_click(rotations: list) -> int:
    password = 0
    dial = 50
    for rot in rotations:
        if 'R' in rot:
            for _ in range(int(rot[1:])):
                if dial == 0:
                    password += 1
                if dial == 99:
                    dial = 0
                else:
                    dial += 1

        elif 'L' in rot:
            for _ in range(int(rot[1:])):
                if dial == 0:
                    password += 1
                    dial = 99
                else:
                    dial -= 1
    
    return password

print(any_click(code))
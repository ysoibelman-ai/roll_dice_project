def check_not_empty(name):
    return name.strip()

def check_valid_num(num,range):
    try:
        num = int(num)
    except ValueError:
        print ("input must be a number")
        return False
    else:
        if not 0<=num<=range:
            print (f"number must be from 0 to {range}")
            return False
        return True
def main():
    result = []
    while True:
        start = input('Enter the starting letter: ')
        end = input('Enter the starting letter: ')
        if len(start) == 1 and start.isalpha():
            start_ord = ord(start)
        else:
            print("Error use letters between A and Z")
            continue
        if len(end) == 1 and end.isalpha():
            end_ord = ord(end)
        else:
            print("Error use letters between A and Z")
            continue
        if start_ord > end_ord:
            print("Starting letter must be before end letter")
        else:
            break
    for char in range(ord(start), ord(end) +1):
            result.append(chr(char))
    print("".join(result))
            
        

    """
    ########################################
    Code Your Program here
    ########################################
    """

    print(*result)

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()

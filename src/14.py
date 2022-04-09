stack = []
max_stack = []

for i in range(int(input())):
    command = input()
    if command == 'pop':
        stack.pop()
        max_stack.pop()

    elif command == 'max':
        print(max_stack[-1])

    else:  # for 'push <num>'
        num = int(command.split(' ')[1])
        stack.append(num)

        if max_stack:
            max_elem = max_stack[-1]
            if max_elem < num:
                max_stack.append(num)
            else:
                max_stack.append(max_elem)
        else:
            max_stack.append(num)

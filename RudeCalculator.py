msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):" 
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"


memory = 0
last_memory = [0]
plus = "+"
minus = "-"
multi = "*"
divide = "/"
operands = [plus, minus, multi, divide]



while True:
    calc = input(f"{msg_0} \n").split()
    a = calc[0]
    b = calc[2]
    if (calc[0] == "M" and calc[2] == "M"):
        print(msg_9 + msg_6)
    
    
    try:
        if calc[0] == "M" and memory >= 0:
            calc[0] = memory
        if calc[2] == "M" and memory >= 0:
            calc[2] = memory

        calc[0] = float(calc[0])
        calc[2] = float(calc[2])

        is_one_digit = -10 < calc[0] < 10, -10 < calc[2] < 10

        ints_check = (a.isdigit() and b.isdigit()) or (calc[0] == "M" and b.isdigit()) or (calc[2] == "M" and a.isdigit()) or (calc[0] == "M" and calc[2] == "M") or (a.rstrip(".0").isdigit() and b.rstrip(".0").isdigit()) or (a.rstrip(".0").isdigit() and calc[2] == "M") or (calc[0] == "M" and b.rstrip(".0").isdigit())

        def laziness():
            if ints_check:
                msg = ""
                if all(is_one_digit):
                    msg = msg + msg_6
                if (int(calc[0]) == 1 or int(calc[2]) == 1) and calc[1] == multi:
                    msg = msg + msg_7
                if (int(calc[0]) == 0 or int(calc[2]) == 0) and (calc[1] == plus or calc[1] == minus or calc[1] == multi):
                    msg = msg + msg_8
                
                if msg != "":
                    print(msg_9 + msg)

        
        if calc[1] in operands:
            if calc[1] == plus:
                memory = calc[0] + calc[2]
                last_memory.append(memory)
                laziness()
                print(memory)
            elif calc[1] == minus:
                memory = calc[0] - calc[2]
                last_memory.append(memory)
                laziness()
                print(memory)
            elif calc[1] == multi:
                memory = calc[0] * calc[2]
                last_memory.append(memory)
                laziness()
                print(memory)
            elif calc[1] == divide:
                if calc[2] != 0:
                    memory = calc[0] / calc[2]
                    last_memory.append(memory)
                    laziness()
                    print(memory)
                else:
                    laziness()
                    print(msg_3)
                    continue

            store = input(f"{msg_4} \n")
            if store == "y":
                try:
                    numbers = [i for i in range(10)]
                    if memory in numbers:
                        usure_1 = input(msg_10)
                        if usure_1 == "y":
                            usure_2 = input(msg_11)
                            if usure_2 == "y":
                                usure_3 = input(msg_12)
                                if usure_3 == "y":
                                    pass
                                else:
                                    memory = last_memory[-2]
                            else:
                                memory = last_memory[-2]
                        else:
                            memory = last_memory[-2]
                except:
                    memory = last_memory[-1]

            elif store == "n":
                memory = last_memory[-2]


            again = input(f"{msg_5} \n")
            if again == "y":
                continue
            else:
                break

        elif calc[1] != any(operands):
            print(msg_2)
    except:
        print(msg_1)
        

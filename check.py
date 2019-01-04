while(1):
    var1, var2 = raw_input("Enter two numbers here: ").split()

    if var1 > var2:
        print("{} jest wieksze od {}".format(var1, var2))
    elif var1 < var2:
        print("{} jest mniejsze od {}".format(var1, var2))
    else:
        print("{} i {} sa rowne".format(var1, var2))

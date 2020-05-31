"""
That module shows the work of BoolFunc,
namely the creation of conjunctival normal form.
"""
from random import choice
from bool_func import BoolFunction



def main():
    """
    Runs the process of making CNF from the the table representation
    of the boolean function.
    :return: None
    """
    var_num = int(input("Please, enter the num of variables:"))
    print("Do you want to enter the function's "
          "values manually(0) or use random(1)?")
    logs = int(input("Please, choose the variant 0 or 1: "))
    if not logs:
        func_value = input("Please, enter the {} function values through "
                           "a space:".format(2 ** var_num)).split()
    else:
        func_value = [str(choice(('0', '1'))) for _ in range(2 ** var_num)]

    bool_func = BoolFunction(var_num, func_value)
    print((var_num + 1) * '------')
    print(bool_func)
    print((var_num + 1) * '------')
    print("Conjunctive normal form:")
    print(bool_func.str_cnf())


if __name__ == '__main__':

    main()

"""
That module realizes ADT for boolean function.
"""
from itertools import product
from tabulate import tabulate


class BoolFunction:
    """
    Class represents the boolean function.
    """
    def __init__(self, var_num, func_value=None):
        """
        Initialization of BoolFunction.
        :param var_num: int
        :param func_value: list
        """
        self.var_num = var_num
        self.func_value = func_value
        self.variables_lst = ['x{}'.format(i + 1)
                              for i in range(var_num)]
        self.table = list()
        self.cnf = list()
        self.table_int = list()
        self.table_creation()
        self.table_to_cnf()
        self.zero_one_table_creation()

    def table_creation(self):
        """
        It creates the table representation
        of the boolean function with defined
        number of variables.
        :return: None
        """
        for i, val in enumerate(product([False, True], repeat=self.var_num)):
            val = list(val)
            val.append(bool(int(self.func_value[i])))
            self.table.append(val)

    def zero_one_table_creation(self):
        """
        It creates the table representation
        of the boolean function with defined
        number of variables.
        :return: None
        """
        for i, val in enumerate(product(['0', '1'], repeat=self.var_num)):
            val = list(val)
            val.append('1' if int(self.func_value[i]) else '0')
            self.table_int.append(val)

    def __str__(self):
        """
        String representation of the boolean function.
        :return: str
        """
        headers_lst = self.variables_lst
        headers_lst.append('F()')
        return tabulate(self.table_int, headers=headers_lst)

    def table_to_cnf(self):
        """
        It creates the  conjunctive normal form
        from the table as the representation
        of boolean function.
        :return: None
        """
        for i in self.table:
            if i[-1]:
                continue
            self.cnf.append([not value for value in i[:-1]])

    def str_cnf(self):
        """
        String representation of CNF.
        :return: str
        """
        result_str = ''
        for collection in self.cnf:
            temp_dnf_lst = [self.variables_lst[i] if collection[i] else '!'
                            + self.variables_lst[i] for i in range(len(collection))]
            temp_dnf_str = "∨".join(temp_dnf_lst)
            result_str += '(' + temp_dnf_str + ')'
        return result_str

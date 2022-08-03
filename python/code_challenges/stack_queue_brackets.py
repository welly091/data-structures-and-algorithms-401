from data_structures.stack import Stack

def multi_bracket_validation(test_str):
    '''
    This function check whether or not the brackets in the input string is balanced.

    :param test_str: the text needs to be checked
    :type test_str: str
    :return: bool
    '''

    dic = {"}": "{", ")": "(", "]": "["}
    my_stack = Stack()

    for i in test_str:
        if i == '{' or i == '(' or i == '[':
            my_stack.push(i)
        # If the stack is empty but encounter a close bracket
        elif dic.get(i) and my_stack.is_empty():
            return False
        # If the top of stack does not equal to the open bracket in dic
        elif dic.get(i) != my_stack.pop():
            return False
    # If the stack is not empty after for loop, meaning there is still open brackets in it.
    if not my_stack.is_empty:
        return False
    return True


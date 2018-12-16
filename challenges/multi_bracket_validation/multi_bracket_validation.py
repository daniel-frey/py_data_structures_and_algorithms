from ...data_structures.stack.stack import Stack


def multi_bracket_validation(string):
    """Check the brackets to be balanced"""
    stack = Stack()

    counter = 0
    for element in string:
        if element == '(' or element == '{' or element == '[':
            stack.push(element)
            counter += 1

        elif element == ')' or element == '}' or element ==']':
            if element == ')' and stack.peek() == '(':
                stack.pop()
                counter -= 1

            elif element == '}' and stack.peek() == '{':
                stack.pop()
                counter -= 1

            elif element == ']' and stack.peek() == '[':
                stack.pop()
                counter -= 1

    if counter == 0 and stack.top is None:
        return True
    else:
        return False

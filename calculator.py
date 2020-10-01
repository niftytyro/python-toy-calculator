"""Toy Calculator in Python"""
from typing import List, Union


def simplify_expression(operator: str, expression_list: List[str]) -> List[str]:
    """Simplifies the expression list by performing the given operator"""
    # Get the position of operator
    position = expression_list.index(operator)
    # Get the numbers before and after operator
    num1 = int(expression_list[position - 1])
    num2 = int(expression_list[position + 1])
    # Calculate expression, for eg. num1 / num2
    result: Union[int, float] = eval(f'{num1} {operator} {num2}')

    # Now replace these 3 items in the list by the result like, replace '4 / 2 + 2' by '2 + 2'
    position_num1 = position - 1
    position_num2 = position + 1
    expression_list = (
        expression_list[:position_num1]
        + [str(result)]
        + expression_list[position_num2 + 1:]
    )

    return expression_list


def main():
    """Main function"""
    expression = input("Enter your expression:")
    expression_list = expression.split()

    for token in expression_list:
        if token in ('+', '-', '*', '/'):
            expression_list = simplify_expression(token, expression_list)

    print(expression_list[0])


if __name__ == "__main__":
    main()

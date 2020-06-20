expression = input("Enter your expression:")
expression_list = expression.split()

for each in expression_list:
    if each == "/":
        # Get the position of '/'
        position = expression_list.index(each)
        # Get the numbers before and after '/'
        num1 = int(expression_list[position - 1])
        num2 = int(expression_list[position + 1])
        # Calculate num1 / num2
        result = num1 / num2
        # Now replace these 3 items in the list by the result like, replace '4 / 2 + 2' by '2 + 2'
        position_num1 = position - 1
        position_num2 = position + 1
        expression_list = (
            expression_list[:position_num1]
            + [str(result)]
            + expression_list[position_num2 + 1 :]
        )
    elif each == "*":
        # Get the position of '/'
        position = expression_list.index(each)
        # Get the numbers before and after '/'
        num1 = int(expression_list[position - 1])
        num2 = int(expression_list[position + 1])
        # Calculate num1 / num2
        result = num1 * num2
        # Now replace these 3 items in the list by the result like, replace '4 / 2 + 2' by '2 + 2'
        position_num1 = position - 1
        position_num2 = position + 1
        expression_list = (
            expression_list[:position_num1]
            + [str(result)]
            + expression_list[position_num2 + 1 :]
        )
    elif each == "+":
        # Get the position of '/'
        position = expression_list.index(each)
        # Get the numbers before and after '/'
        num1 = int(expression_list[position - 1])
        num2 = int(expression_list[position + 1])
        # Calculate num1 / num2
        result = num1 + num2
        # Now replace these 3 items in the list by the result like, replace '4 / 2 + 2' by '2 + 2'
        position_num1 = position - 1
        position_num2 = position + 1
        expression_list = (
            expression_list[:position_num1]
            + [str(result)]
            + expression_list[position_num2 + 1 :]
        )
    elif each == "-":
        # Get the position of '/'
        position = expression_list.index(each)
        # Get the numbers before and after '/'
        num1 = int(expression_list[position - 1])
        num2 = int(expression_list[position + 1])
        # Calculate num1 / num2
        result = num1 - num2
        # Now replace these 3 items in the list by the result like, replace '4 / 2 + 2' by '2 + 2'
        position_num1 = position - 1
        position_num2 = position + 1
        expression_list = (
            expression_list[:position_num1]
            + [str(result)]
            + expression_list[position_num2 + 1 :]
        )

print(expression_list[0])

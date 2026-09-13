
In Python every value is considered either True or False. Truthiness is basically if a value is evaluetad as True boolean type. It is used in conditional statements.

A for loop is used if you know the number of iterations in advance. 
A while loop is used when you do not know how many times it will run, repeating indefinitely until a specific condition changes to false.

A break statement instantly terminates the entire loop and jumps to the code outside it. 
A continue statement skips only the remaining code in the current iteration and immediately jumps to the start of the next cycle.

Chose a while loop over a for loop when the exact number of iteraions is unknown in advace and depends on a dynamic condition rather than a fixed range or collection. This setup is ideal for scenarios like validating user input, streaming data until a file ends, or running continuous game engines that loop indefiitely until a quit signal is detected. 

In modern software development, early returns and goard clauses are overwhelmingly preferred for mainstream coding. The reduction in cognitive load adn cleaner formatting almost always outweighs the traditional rule of having a single exit point.

# Deeply Nested Structure
def process_payment(user, order):
    if user.is_active:
        if order.is_valid:
            if user.has_funds(order.total):
                # Core logic is buried 3 levels deep
                transaction = execute_payment(user, order)
                return transaction
            else:
                return "Insufficient funds"
        else:
            return "Invalid order"
    else:
        return "Inactive user"

# Guard Clauses / Early Returns
def process_payment(user, order):
    if not user.is_active:
        return "Inactive user"
        
    if not order.is_valid:
        return "Invalid order"
        
    if not user.has_funds(order.total):
        return "Insufficient funds"

    # Core logic stays completely unindented
    return execute_payment(user, order)





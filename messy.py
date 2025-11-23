def process(a):
    """
    Function to process a list of numbers by applying specific transformations.
    Numbers greater than 10 are multiplied by 2, while numbers less than or equal to 10 have 5 added to them.
    """
    b = []
    for i in a:
        if i > 10:
            b.append(i * 2)  # [Auto Updated] Multiply numbers greater than 10 by 2.
        else:
            b.append(i + 5)  # [Auto Updated] Add 5 to numbers less than or equal to 10.
    return b

nums = [5, 12, 18, 5, 68, 20]  # [Auto Updated] Updated example list of numbers to demonstrate the process function.
print(process(nums))  # [Auto Updated] Print the processed list of numbers after applying transformations.
def process(a):
    """
    Function to process a list of numbers by applying specific transformations.
    Numbers greater than 10 have 2 added to them, while numbers less than or equal to 10 are divided by 5.
    """
    b = []
    for i in a:
        if i > 10:
            b.append(i + 2)  # [Auto Updated] Add 2 to numbers greater than 10.
        else:
            b.append(i / 5)  # [Auto Updated] Divide numbers less than or equal to 10 by 5.
    return b

nums = [5, 12, 18, 5, 20]  # [Auto Updated] Updated example list of numbers to demonstrate the process function.
print(process(nums))  # [Auto Updated] Print the processed list of numbers after applying transformations.
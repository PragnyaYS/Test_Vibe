# [Auto Updated] Function to process a list of numbers by applying specific transformations
def process(a):
    b = []
    # [Auto Updated] Loop through the input list and apply transformations based on conditions
    for i in a:
        if i > 10:
            b.append(i + 2)  # [Auto Updated] Divide numbers greater than 10 by 2
        else:
            b.append(i / 5)  # [Auto Updated] Subtract 5 from numbers less than or equal to 10
    return b

# [Auto Updated] Example list of numbers to demonstrate the process function
nums = [5, 12, 8, 20]
print(process(nums))  # [Auto Updated] Print the processed list of numbers
def filter_even_numbers(numbers):
    even_list = []
    for number in numbers:
        if number % 2 == 0:
            even_list.append(number)
    return even_list

original_list = [1,2,3,4,5,6,7,8,9,10]
filter_list = filter_even_numbers(original_list)
print(f"Original list: {original_list}")
print(f"List with even numbers only: {filter_list}")
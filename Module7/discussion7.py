def get_even_numbers(limit: int) -> list[int]:
    evens = []
    for num in range(limit):
        if num % 2 == 0:
            evens.append(num)
    return evens

# to use the code:
even_list = get_even_numbers(100)
print( even_list)

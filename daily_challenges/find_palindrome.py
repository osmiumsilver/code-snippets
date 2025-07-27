def find_palindrome(string):
    length = len(string)
    middle_index = length // 2
    first_half = string[:middle_index]
    second_half = string[middle_index:] if length % 2== 0 else string[middle_index+1:]
    return first_half == second_half[::-1]

print(find_palindrome("racecar"))
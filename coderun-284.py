def get_firs_letter(a: str) -> str:
    return a[0]


command_amount = int(input())

list_of_commands = []

for e in range(command_amount):
    list_of_commands.append(input())

first_letters = list(map(get_firs_letter, list_of_commands))

max_count = 0
letter = ""

for e in first_letters:
    if first_letters.count(e) > max_count:
        max_count = first_letters.count(e)
        letter = e

print(letter)
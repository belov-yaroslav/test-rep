key_amount = int(input())
str_key_amount = []
for e in range(key_amount):
    str_key_amount.append(str(e+1))

str_key_limits = input()
split_str_key_limits = str_key_limits.split()
int_key_limits = []
for e in split_str_key_limits:
    int_key_limits.append(int(e))

key_limit_dict = {}

for i in range(key_amount):
    key_limit_dict[str_key_amount[i]] = int_key_limits[i]

press_amount = int(input())

press_seq = input()
split_press_seq = press_seq.split()

for e in split_press_seq:
    key_limit_dict[e] -= 1

for e in str_key_amount:
    if(key_limit_dict[e] < 0):
        print("YES")
    else:
        print("NO")


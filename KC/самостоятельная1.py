input_data = 'five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'
data = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
        'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
        'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'twenty one': 21}
data_split = set(input_data.split(' '))
print(data_split)
values_list = []
for val in data_split:
    values_list.append(data[val])
print(values_list)
values_list.sort()
print(values_list)

for i in range(0, len(values_list), 2):
    if i + 1 <= len(values_list) - 1:
        print(f'product = {(values_list[i] * values_list[i+1])}')
    if i + 2 <= len(values_list) - 1:
        print(f'summary = {(values_list[i+1] + values_list[i+2])}')

print(f' summary all numbers = {sum(i for i in values_list if i % 2 != 0)}')

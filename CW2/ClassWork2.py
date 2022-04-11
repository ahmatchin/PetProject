unsort_lst = ['1', '11', '12', '22', '2', '13', '30', '33']
unsort_lst.sort(key=lambda x: int(x))
print(list(filter(lambda x: int(x)**2 % 2 == 0, unsort_lst)))

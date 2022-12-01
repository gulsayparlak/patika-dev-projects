# SORU 1
# Bir listeyi düzleştiren (flatten) fonksiyon yazın.
# Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi,
# non-scalar verilerden de oluşabilir. Örnek olarak:
# input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
# output: [1,'a','cat',2,3,'dog',4,5]

list1 = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
flatten_list = []


def flatten(l):
    for sublist in l:
        if type(sublist) == list:
            flatten(sublist)
        else:
            flatten_list.append(sublist)
    return flatten_list


print(flatten(list1))

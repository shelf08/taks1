# Составить новый список из первых n минимальных чисел переданного списка, взятых по одному разу.
# Если в переданном списке нет n различных чисел, то итоговый список будет короче n.
#
# Примеры:
#
# ({ 7, 2, 3, 2, 2, 6, 5, 7, 8, 8, 3 }, 4) → { 2, 3, 5, 6 }
# ({ 3, 3, 7, 3, 5, 3 }, 5) → { 3, 5, 7 }


try:
    input_f = open('1.txt', 'r')
    lines = input_f.readlines()
    a = [int(num) for num in lines[0].split(',')]
    input_f.close()
except FileNotFoundError as err:
    print("File not found or it cannot be read!")
    print(err)

n = input()
b = sorted(set(a))[:int(n)]

output_f = open('2.txt', 'w')
output_f.write(str(b))
output_f.close()
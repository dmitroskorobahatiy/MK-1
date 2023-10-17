import random
min = int(input("Мінімальне значення:")) #вводимо мінімальне значення
max = int(input("Максимальне значення:")) #вводимо максимальне значення
N =int(input("кількість рядків:")) # вводимо кількість рядків
matrix = [[random.randint(min,max) for _ in range(N)] for _ in range(N)] #сортування матриці

# Сортуємо рядки за середнім значенням
def calculate_average(list):
    return sum(list) / N
sorted = sorted(matrix, key=calculate_average)

# Виводимо відсортований масив та середнє значення рядків.
print("Відсортований масив та середні значення рядків:")
for list in sorted:
    print(list, "- ", sum(list) / N)


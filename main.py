# firstloop3
# Reverse a given integer number

num = '76542'

reverse = ''
for value in range(len(num), 0, -1):
   reverse = reverse + num[value-1]
reverse = int(reverse)
print(reverse)

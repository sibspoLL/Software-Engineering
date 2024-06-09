## Палиндромом называется строка, которая пишется одинаково слева направо и справа налево

data=input("Введите слово: ")
reverse=data [::-1]
def is_palindrome(data):
    while True:
        if data[::1]==reverse:
            print(data ,"YES")
            return True
            break
        if data !=reverse:
            print(data ,"NO")
            return False
            break


print(is_palindrome(data))
# https://docs.python.org/3.11/library/doctest.html?highlight=doctest
# https://docs.python.org/3.11/library/unittest.html?highlight=unittest
# https://github.com/luizomf/python-tests


from calculadora import soma  # type: ignore

# print(soma(10, 20))
# print(soma(-10, 20))
# print(soma("15", 15))

# try:
#    print(soma("15", 15))
# except TypeError as e:
#    print("Conta inválida")
#     print(e)

try:
    print(soma("15", 15))  # type: ignore
except AssertionError as e:
    print(f"Conta inválida: {e}")

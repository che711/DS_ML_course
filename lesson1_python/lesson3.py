def my_func(name="NO_NAME"):
    """just print 'Hello, + name'"""
    print(f"Hello, {name}")

my_func("Tonny")
my_func()

def square(x):
    return (x**2)

result = square(3)
print(result)

print(type(result))

# lambda - похожа на функции, но не имеют названий и заускаются только один раз
lambda var: var*2

def times_two(var): return var*2
times_two(11)

st = "test Text and SomeThing ALSe"
st.lower()
st.upper()
st.split() # разбивает строку и превращает ее в словарь со строками
tweet = "Hello, #sports test data #just for fun"
tweet.split()
tweet.split('#')
tweet.split(' ')
tweet.split('#')[1]
tweet.split('#')[-1]

d = {"k1":"v1", "k2":"v2"}
d.keys()
d.items() # словарь не хранят порядок поэтому возвращаются в произвольном виде

my_list = [1, 2, 3]
print(my_list)
# извлекает **по умолчанию**последний элемент списка
last = my_list.pop()
print(my_list)
print(last)
print(my_list)


my_list=[1, 2, 3, 4]
print(my_list)
# my_list.pop(0) - извлекает из списка my_list нулевой элемент и сохраняет в переменную
first = my_list.pop(0)
print(my_list)
print(first)

print("x" in [1, 2, 3])

print("x" in my_list)
print(2 in my_list)


from pprint import pprint

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

print(f"\n")
# извлечь слово "hello"
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
list_1=[]
list_2=[]
list_3=[]
list_4=[]
for value in d.values():
    list_1.append(value)
    for itim in list_1:
        list_2.append(itim)
        for items in list_2:
            list_3.append(items)
            for data in list_3:
                list_4 = data[3]
                for hello in list_4.values():
                    hello_word = hello[3]
                    for finish in hello_word.values():
                        for test in finish:
                            if test == "hello": print(test)


def domainGet(email):
    return email.split('@')[-1]

email_string = domainGet('user@domain.com')
print(email_string)

tuple = ("connot", "be", "changed")
list = ["can", "be", "updated", "or", "changed"]
print(f"Tuple: {tuple}. List: {list}")

def findDog(st):
    return str.split('dog')
print(f"Dogs in the line: {len(findDog('Is there a Dog here?'))}")


def countDog(st):
    dog_counter=0
    dogline = st.split(' ')
    for doggy in dogline:
        if doggy == 'dog': dog_counter += 1
    return dog_counter

Dogs = countDog('This dog runs faster than the other dog dude! dog dog dog dog')
print(f"Dogs: {Dogs}")
print(f"Final exam")
def caught_speeding(speed, is_birthday=False):
    '''Counter for your speeed accourding to your birthday'''
    print(f"speed: {speed}, boolean: {is_birthday}")
    if is_birthday: speed += 5
    if speed in range(61, 80): return (f"Small tax, speed: {speed}")
    elif speed <=60: return (f"There are no any taxes, speed: {speed}")
    else: return (f"Big tax, speed: {speed}")

print(f"{caught_speeding(80, True)}")






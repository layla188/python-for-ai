#comment 
first_num = 30 #another comment
name = "lolo"

if first_num > 0:
    print("num is big")

    """"
  this is multi line code
  go on
  whda kman

    """
    power = 10 ** 2
    sub = 10 - 3

    string = "eh ya lolo"
    long_string = """
    hello
    hi lolo
    now what
    """
    long_dash = "-" *20
    print(long_string)
    print(long_dash)
    len(long_string)
    
    is_true = True
    age = 18
    can_vote = age >= 19
    is_18 = age == 18

    name = "layla lolo"
    strr = f"my name is {name} yasser"
    name.upper()
    name.lower()
    name.title()
    
    temp = 31
    if temp > 30:
        print("its very hot")
    elif  temp > 14:
        print("its hot")
    else:
        print("cold")

#loooooooooooopppppp
for i in range(5):
    print(i)
    print("hello")

for x in range(1, 6):
    print(x)
    

#############################
    agge = 1
    booll = False
    my_list = ["lolo", 18, agge, True, booll]
    name = my_list[0:2]
    has = my_list[-1]
    my_list.insert(1, "layla")

    ####################dic
    person = {
        "name": "lolo",
        "age": "22",
        "bol": "True"
    }

    person ["name"] = "nono"
    person["for"] = "dodo"
    del person ["for"]
    person.keys()
    person.values()
    person.items()
    print(person.get("job", "Unknown"))
    person.update({"age": 31, "bol": "Engineer"})

    ##################################sets
    fruits = set(["apple", "banana", "banana", "orange"])
    scores = [85, 90, 85, 92, 90]
    uniq =set(scores) #remove dublicate
#sets could use {}and []
    colors = {"red", "blue"}
    colors.add("red")
    colors.add("yellow")
    colors.remove("blue")    # Error if not found
    colors.discard("yellow") # No error if not found
    #error handling
    try:
        age = int(input("Enter your age: "))
        print(f"In 10 years, you'll be {age + 10}")
    except ValueError:
        print("Please enter a number")
import time
# def dec(func):
#     def wrapper(n,m):
#         if(m/n)<int(60):
#             print("good")
#         return func(n,m)
#     return wrapper
            

# @dec
# def avg(numberOfMarks,Sum):
#     return Sum/numberOfMarks

# # print(avg(10,350))





# def dec(func):
#     def wrapper():
#         start=time()
#         func()
#         end=time()
#         print(end-start)
#     return wrapper

# @dec
# def loop():
#     for i in range(1,25000):
#         print(i)
# loop()

def timer(func):
    def wrapper(*args, **kwargs):
        kwargs.update({"a":10})
        return func(*args, **kwargs)
        
    return wrapper
        

@timer
def hello(a,b):
    print("Hello: ")
    time.sleep(2)
    print(a*b)
    
@timer

def hello1():
    print("Hello: ")
    time.sleep(4)

hello(a=5,b=6)
# hello1()

class MyClass(object):
    def __enter__(self):
        print('we entered class')
        return self
    
    def __exit__(self, exc_type, exc_val,exc_tb):
        print('we exited')
        

with MyClass() as mc:
    print("we are in thr body class")
    try:
        while True:
            print(5)
    except KeyboardInterrupt:
        print()
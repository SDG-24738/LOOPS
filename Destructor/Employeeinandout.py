class employee:
    def __init__(self):
        print('employee created')
    def __del__(self):
        print("Destructor called")
def create_obj():
    print('Making Oject...')
    obj = employee()
    print('function end...')
    return obj
print('callig Create_obj() function...')
obj = create_obj()
print('Program End...')
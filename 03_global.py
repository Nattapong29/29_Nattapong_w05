counter = 0

def increment():
    '''เพิ่มค่า Counter ทีละ1 '''
    global counter
    counter += 1
    print(f"counter : {counter}")
    
def reset_counter(): 
    '''reset counter ไห้เป็น 0'''
    global counter
    counter =0
    print(f"counter รีเซ็ตแล้ว ")
    
    
    increment()
    increment()
    increment()
    
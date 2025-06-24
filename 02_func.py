# รับ paramitter
'''def =ชื่อฟังค์ชั่น(paramitter)
 parametter1 + parametter 2 = xxx 
 
 '''
 
def get_name(name):
    '''show name from parametter'''
    print(f"Hello !!! : {name}")
    


def add_num(a,b):
    '''ฟังค์ชั่นบวกเลข '''
    result = a + b
    return result
 
def rect_cal(width, length):
    '''ฟังค์ชั่นหาพื้นที่สี่เหลี่ยมและเส้นกรอบ'''
    area = width * length   
    frame = 2* (width + length)
    return area, frame


width = 3 
length = 10

area ,fream = rect_cal(width,length)
print(f"พื้นที่สี่เหลี่ยม = {area}"," เส้นกรอบ= {fream}")
     
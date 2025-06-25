import math 

pi = math.pi

def cal_circle_area(rasius):
    '''คำนวน พท. วงกลม'''
    return pi * radius  ** 2 
radius = 10 
result = cal_circle_area(radius)

def cal_rect_area(width,lengh):
    '''คำนวน พท 4เหลี่ยม'''
    return width * lengh

print(result)

# ()
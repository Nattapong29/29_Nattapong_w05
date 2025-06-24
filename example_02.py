def calcurate_salary(salary, tax, ot_time, ot_rate):
    gross_pay = salary + (ot_time * ot_rate)
    tax_pay = gross_pay * tax
    net_pay = gross_pay - tax_pay
    return net_pay

emp_1 = calcurate_salary(15000, 0.07, 10, 200)
print("คำนวนภาษีคนที่ 1")
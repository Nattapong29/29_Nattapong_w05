# คำนวนภาษี 1
salary_1 = 1500
tax = 0.07
ot_time = 10
ot_rate = 200
# 2
gross_pay = salary_1 +(ot_time * ot_rate)
tax_pay = gross_pay * tax
net_pay = gross_pay - tax_pay
print(f"จ่ายคนที่ 1  :{net_pay}")

salary = 2000
tax = 0.07
ot_time = 1500
ot_rate = 200

gross_pay = salary +(ot_time * ot_rate)
tax_pay = gross_pay * tax
net_pay_1 = gross_pay - tax_pay
print(f"จ่ายคนที่ 2  :{net_pay_1}")


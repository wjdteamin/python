# 월급(300)을 입력받아 1년치의 소득세(118.8)와 소득세를 제외한 연봉(3481.2)을 출력하시오
# 소득세율 3.3%

#literal 
TAX_RATE = 0.033
month_pay = int(input("월급? : "))
year_pay = month_pay * 12

print(f"연봉 : {year_pay}원")
tax = year_pay * TAX_RATE
print(f"실수령액 : {year_pay-tax}원")
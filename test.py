# 房贷计算器
price =1.023;
year=eval(input("输入你的年数： "));
# 每年存款金额
salary=eval(input("每年攒钱数量： "));
SumMoney=40;
for i in range(year):
    SumMoney=(SumMoney+salary)*price;
    print(SumMoney);
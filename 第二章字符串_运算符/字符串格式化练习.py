name = "取经团队"
stock_price = 500
stock_code = 9981
rate = 1.2
growth_days = 10

print(f"公司:{name}, 股票代码:{stock_code}, 当前股价:{stock_price}")
print("每日增长系数是:%.1f, 经过%d天的增长,股票价格达到了:%.2f" % (rate, growth_days, (stock_price*rate**growth_days)))
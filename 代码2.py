cart = []  # 存储商品信息：[(名称, 价格), ...]
print("欢迎使用智能购物车！请输入商品名称和价格，输入'done'结束")
while True:
    name = input("商品名称: ")
    if name.lower() == "done":
        break
    price = float(input("商品价格: "))
    cart.append((name, price))  # 使用元组存储商品信息
total_original = sum(price for _, price in cart)# 计算原总价
if total_original >= 500:
    discount_rate = 0.8
    discount_name = "8折"
elif total_original >= 300:
    discount_rate = 0.9
    discount_name = "9折"
elif total_original >= 100:
    discount_rate = 0.95
    discount_name = "95折"
else:
    discount_rate = 1.0
    discount_name = "无折扣"
total_discounted = total_original * discount_rate
saved = total_original - total_discounted# 计算折扣后价格
print("\n===== 购物清单 =====")
for i, (name, price) in enumerate(cart, 1):
    print(f"{i}. {name}: ￥{price:.2f}")

print("\n===== 结算信息 =====")
print(f"原总价: ￥{total_original:.2f}")
print(f"折扣: {discount_name}")
print(f"折扣后价格: ￥{total_discounted:.2f}")
print(f"节省金额: ￥{saved:.2f}")
import random
target = random.randint(1, 100)
chances = 5
print("欢迎来到猜数字游戏！")
print("我已经想了一个1到100之间的数字，你有5次机会猜中它。")
for attempt in range(1, chances + 1):
    guess = int(input(f"\n第{attempt}次猜测，请输入你的数字："))#f-string 字符串格式化和将用户输入转换为整数
    if guess < target:
        print("太小了！")
    elif guess > target:
        print("太大了！")
    else:
        print("恭喜你，猜对了！")
        Break# 猜测正确，输出成功信息并使用break退出循环

else:
    print(f"\n很遗憾，机会用完了！正确答案是：{target}")
print("游戏结束，谢谢参与！")
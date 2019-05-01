import sys
import random

print("*" * 10, "start", "*" * 10)

goal = 30
while True:
    try:
        dummy = input("サイコロを降ってください (止めるときはqを押してください)")
    except (KeyboardInterrupt, EOFError):
        print("止められませんよ")
    if dummy == "q":
        print("ゲームを終わりにします。")
        sys.exit(1)
    dice_num = random.randint(1, 6)
    print("サイコロの目は", dice_num, "です。")
    goal -= dice_num
    if goal > 0:
        print("ゴールまで", goal, "です。")
    else:
        print("ゴールしました")
        sys.exit(0)

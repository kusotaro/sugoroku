import sys

print("*" * 10, "start", "*" * 10)

while True:
    print("サイコロを降ってください (止めるときはqを押してください)")
    try:
        dummy = input()
    except KeyboardInterrupt as e:
        import pdb

        print("文字を入れろよデコスケ野郎！")
    if dummy == "q":
        print("ゲームを終わりにします。")
        sys.exit(1)
    print("入力された値は", dummy, "です。")
print("end!")


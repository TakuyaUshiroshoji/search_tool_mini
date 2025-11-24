items = ["apple", "banana", "grape", "pineapple", "orange"]

keyword = input("検索したいワードを入力してください :")

total_number = 0
for item in items:
    if keyword in item:
        print("一致:", item)
        total_number += 1

print(total_number,"件ヒットしました。")

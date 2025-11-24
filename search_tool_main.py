import json

items = []
with open('data.txt', 'r', encoding='utf-8') as file:
    for line in file:
        items.append(line.strip())

keyword = input("検索したいワードを入力してください : ")

search_result = []
total_number = 0
for item in items:
    if keyword in item:
        print("一致:", item)
        search_result.append(item)
        total_number += 1

print(total_number, "件ヒットしました。")

data = {
    "keyword": keyword,
    "hits": search_result,
    "count": total_number
}
with open('search_result.json', 'w', encoding='utf-8') as out_file:
    json.dump(data, out_file, ensure_ascii=False, indent=2)

print("search_result.json に保存しました。")
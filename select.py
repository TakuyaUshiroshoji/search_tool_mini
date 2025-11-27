def select():
    select_number = ["1:OR検索", "2:AND検索"]
    for num in select_number:
        print(num)
    while True:
        number_str = input("検索方法を選択してください : ")
        if not number_str.isdigit():
            print("数字を入力してください")
            continue
        number = int(number_str)

        if 1 <= number <= len(select_number):
            return number
        else:
            print(f"{1} ~ {len(select_number)}を選んでください")
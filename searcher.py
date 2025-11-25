def search_items(items, keyword):
    """"itemsの中からkeywordで検索して結果を返す"""
    results = []
    for item in items:
        if keyword.lower() in item.lower():
            results.append(item)

    return results
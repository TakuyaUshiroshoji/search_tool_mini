def search_items(items, keywords):
    """"itemsの中からkeywordsでOR検索して結果を返す"""
    results = []
    for item in items:
        lower_item = item.lower()

        if any(kw.lower() in lower_item for kw in keywords):
            results.append(item)
    return results

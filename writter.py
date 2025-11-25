import json

def save_results(file_path, keyword, hits):
    """jsonファイルに検索結果を保存する"""
    data = {
        "keyword": keyword,
        "hits": hits,
        "count": len(hits)
    }

    with open(file_path, 'w', encoding='utf-8') as out_file:
        json.dump(data, out_file, ensure_ascii=False, indent=2)
    print(file_path, "に保存しました。")
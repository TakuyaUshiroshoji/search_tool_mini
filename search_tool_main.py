from loader import load_items
from searcher import search_items
from writter import save_results

def main():
    items = load_items('data.txt')
    keyword = input("検索したいワードを入力してください : ")
    hits = search_items(items, keyword)
    print(len(hits), "件ヒットしました。")
    save_results('search_result.json', keyword, hits)

if __name__ == "__main__":
    main()
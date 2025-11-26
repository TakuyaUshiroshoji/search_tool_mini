from loader import load_items
from searcher import search_items
from writter import save_results

def main():
    items = load_items('data.txt')
    keywords = []
    keywords = (input("検索したいワードを入力してください : ").split())
    hits = search_items(items, keywords)
    print(len(hits), "件ヒットしました。")
    save_results('search_result.json', keywords, hits)

if __name__ == "__main__":
    main()
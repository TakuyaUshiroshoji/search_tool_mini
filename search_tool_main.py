from loader import load_items
from searcher import or_search_items, and_search_items
from writter import save_results
from select import select

def main():
    items = load_items('data.txt')
    keywords = []
    keywords = (input("検索したいワードを入力してください : ").split())
    
    number = select()
    if number == 1:
        hits = or_search_items(items, keywords)
    elif number == 2:
        hits = and_search_items(items, keywords)

    print(len(hits), "件ヒットしました。")
    save_results('search_result.json', keywords, hits)

if __name__ == "__main__":
    main()
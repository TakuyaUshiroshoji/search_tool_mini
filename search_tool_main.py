from loader import load_items
from searcher import or_search_items, and_search_items
from writter_json import save_json
from writter_csv import save_csv
from cli import get_parser

def main():
    args = get_parser().parse_args()
    print(args.mode)
    print(args.keywords)

    items = load_items('data.txt')
    search_func = and_search_items if args.mode == "AND" else or_search_items
    hits = search_func(items, args.keywords)

    print(len(hits), "件ヒットしました。")
    save_json('search_result.json', args.keywords, hits)
    save_csv('search_result.csv', args.keywords, hits)

if __name__ == "__main__":
    main()
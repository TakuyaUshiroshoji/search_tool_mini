from loader import load_items
from searcher import or_search_items, and_search_items
from writter_json import save_json
from writter_csv import save_csv
from cli import get_parser
import sys

def main():
    args = get_parser().parse_args()
    
    print(args.mode)
    print(args.keywords)

    try:
        items = load_items(args.file)
    except FileNotFoundError as e:
        print(f"ファイルが見つかりません: {args.file}", file=sys.stderr)
        return

    search_func = and_search_items if args.mode == "AND" else or_search_items
    hits = search_func(items, args.keywords)
    if not hits:
        print("0件でした。条件を変えてください")
        return

    print(len(hits), "件ヒットしました。")

    try:
        save_json('search_result.json', args.keywords, hits)
    except Exception as e:
        print("JSONの保存に失敗(file = search_result.json):", e, file = sys.stderr)
        
    try:
        save_csv('search_result.csv', args.keywords, hits)
    except Exception as e:
        print("csvファイルの保存に失敗(file = search_result.csv):", e, file = sys.stderr)

if __name__ == "__main__":
    main()
import argparse

def get_parser():
    parser = argparse.ArgumentParser(description="検索ツール")
    parser.add_argument(
        "--mode",
        choices=["AND", "OR"],
        default="AND",
        help="AND検索 or OR検索を選択"
        )
    
    parser.add_argument(
        "--keywords",
        required=True,
        nargs="+",
        help="検索キーワード(複数可)"
        )
    parser.add_argument(
        "--file",
        required=True,
        help="検索するファイルを指定"
    )
    
    return parser
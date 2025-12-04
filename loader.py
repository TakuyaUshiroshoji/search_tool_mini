def load_items(file_path):
    """ファイルから行を読み込んでリストにして返す"""
    items = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            items.append(line.strip())
    
    return items
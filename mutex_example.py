import threading
import time

# ミューテックス（Lock）とグローバル変数を定義
lock = threading.Lock()
_shared_counter = 0  # 共有リソース

def increment(name):
    """
    カウンターをインクリメントする関数：ミューテックスで排他制御
    """
    global _shared_counter
    print(f"{name} がロックの取得を試みています")
    
    with lock:  # withステートメントでクリティカルセクションを保護
        print(f"{name} がロック取得 (カウンター更新)")
        val = _shared_counter
        time.sleep(0.5)  # 意図的な処理遅延でレースコンディションを検証
        _shared_counter = val + 1
        print(f"{name} 更新後のカウント: {_shared_counter}")

# メイン処理
if __name__ == "__main__":
    threads = []
    
    # 10個のスレッドを作成してカウンターを並行してインクリメント
    for i in range(10):
        t = threading.Thread(target=increment, args=(f"Thread-{i+1}",))
        threads.append(t)
        t.start()
    
    # すべてのスレッドの終了を待機
    for t in threads:
        t.join()
    
    print(f"最終カウント: {_shared_counter}")
    print("ミューテックスにより正しく10回インクリメントされました" if _shared_counter == 10 else "排他制御に問題があります")
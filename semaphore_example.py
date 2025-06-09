import threading
import time

# セマフォを作成（同時実行数を2に制限）
sem = threading.Semaphore(2)

def worker(name):
    """
    ワーカー関数: セマフォを使用してリソースへのアクセスを制御
    """
    print(f"{name} が実行待ち... アクセス権の取得を待機")
    sem.acquire()
    try:
        print(f"{name} がリソースを使用中")
        time.sleep(2)  # 2秒間のリソース使用をシミュレート
    finally:
        print(f"{name} がリソースを解放")
        sem.release()

# メイン処理
if __name__ == "__main__":
    threads = []
    
    # 5つのタスクを作成
    for i in range(5):
        t = threading.Thread(target=worker, args=(f"Task-{i+1}",))
        threads.append(t)
        t.start()
    
    # すべてのスレッドの終了を待機
    for t in threads:
        t.join()
    
    print("すべてのタスクが完了しました")
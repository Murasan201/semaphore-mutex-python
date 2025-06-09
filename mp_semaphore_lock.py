from multiprocessing import Process, Semaphore, Lock, Manager
import time

# マルチプロセス用の共有リソースとセマフォを初期化
mgr = Manager()
shared_list = mgr.list()
sem = Semaphore(1)  # 一度に1つのプロセスのみアクセス許可
lock = Lock()

def mp_worker(name):
    """
    マルチプロセス用ワーカー関数：セマフォで共有リストへのアクセスを制御
    """
    print(f"{name} がセマフォの取得を試みています")
    sem.acquire()
    try:
        print(f"{name} が共有リストに追加中")
        shared_list.append(name)
        time.sleep(1)  # 処理時間をシミュレート
        print(f"{name} が共有リストへの追加を完了")
    finally:
        sem.release()
        print(f"{name} がセマフォを解放")

def mp_worker_with_lock(name, shared_dict):
    """
    ロック使用例：共有辞書への安全なアクセス
    """
    with lock:
        print(f"{name} がロックを取得して辞書を更新")
        shared_dict[name] = f"プロセス {name} の実行時刻: {time.time()}"
        time.sleep(0.5)

# メイン処理
if __name__ == "__main__":
    print("=== セマフォを使用したマルチプロセス例 ===")
    
    processes = []
    
    # 3つのプロセスを作成（セマフォ例）
    for i in range(3):
        p = Process(target=mp_worker, args=(f"Proc-{i+1}",))
        processes.append(p)
        p.start()
    
    # すべてのプロセスの終了を待機
    for p in processes:
        p.join()
    
    print(f"共有リストの内容: {list(shared_list)}")
    
    print("\n=== ロックを使用したマルチプロセス例 ===")
    
    # 共有辞書の例
    shared_dict = mgr.dict()
    processes2 = []
    
    # 3つのプロセスを作成（ロック例）
    for i in range(3):
        p = Process(target=mp_worker_with_lock, args=(f"Worker-{i+1}", shared_dict))
        processes2.append(p)
        p.start()
    
    # すべてのプロセスの終了を待機
    for p in processes2:
        p.join()
    
    print("共有辞書の内容:")
    for key, value in shared_dict.items():
        print(f"  {key}: {value}")
    
    print("マルチプロセス処理が完了しました")
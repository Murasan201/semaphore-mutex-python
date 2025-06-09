# 要件定義書: semaphore-mutex-python レポジトリ

**リポジトリURL**: [https://github.com/Murasan201/semaphore-mutex-python](https://github.com/Murasan201/semaphore-mutex-python)

## 1. 背景・目的

本プロジェクトは、Pythonにおけるセマフォ（Semaphore）およびミューテックス（Mutex）を利用した排他制御サンプルコードを提供し、Raspberry Piや一般的なLinux/Windows環境でのマルチスレッド・マルチプロセス処理の安定性向上を支援します。

## 2. 適用範囲

* 対象コード: `semaphore_example.py`, `mutex_example.py`, `mp_semaphore_lock.py`
* 環境: Python 3.6以上、Raspberry Pi OS、Ubuntu 22.04以上、Windows 10/11

## 3. 用語定義

* **セマフォ (Semaphore)**: 同時にアクセス可能なリソース数を制限する同期機構
* **ミューテックス (Mutex)**: 一度に一つのタスクのみがアクセス可能な排他制御機構
* **スレッド (Thread)**: プロセス内で並行実行される処理単位
* **プロセス (Process)**: OSから独立した実行単位

## 4. 機能要件

### 4.1 セマフォ制御サンプル

* 同時実行数を2に制限できること
* `acquire()` による待機、`release()` によるリソース解放が動作すること

#### サンプルコード: semaphore\_example.py

```python
import threading
import time

sem = threading.Semaphore(2)  # 同時実行を2までに制限

def worker(name):
    print(f"{name} が実行待ち... アクセス許可を取得します")
    sem.acquire()
    try:
        print(f"{name} がリソースを使用中")
        time.sleep(2)
    finally:
        print(f"{name} がリソースを解放")
        sem.release()

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(f"Task-{i+1}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
print("すべてのタスクが完了しました")
```

### 4.2 ミューテックス制御サンプル

* 共有カウンタをスレッド間で安全に更新できること
* `with lock` を用いたクリティカルセクションが正しく動作すること

#### サンプルコード: mutex\_example.py

```python
import threading
import time

lock = threading.Lock()
_shared_counter = 0  # 共有リソース

def increment(name):
    global _shared_counter
    print(f"{name} がロックを取得しようとしています")
    with lock:
        print(f"{name} がロック取得 (カウントを更新)")
        val = _shared_counter
        time.sleep(0.5)  # 意図的な処理遅延
        _shared_counter = val + 1
        print(f"{name} 更新後のカウント: {_shared_counter}")

threads = []
for i in range(10):
    t = threading.Thread(target=increment, args=(f"Thread-{i+1}",))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print(f"最終カウント: {_shared_counter}")
```

### 4.3 マルチプロセス制御サンプル

* プロセス間で共有可能なリストに正しく要素追加できること
* `Semaphore(1)` によるプロセス単位の排他制御が動作すること

#### サンプルコード: mp\_semaphore\_lock.py

```python
from multiprocessing import Process, Semaphore, Lock, Manager
import time

mgr = Manager()
shared_list = mgr.list()
sem = Semaphore(1)
lock = Lock()

def mp_worker(name):
    sem.acquire()
    try:
        print(f"{name} がリストに追加中")
        shared_list.append(name)
        time.sleep(1)
    finally:
        sem.release()

processes = []
for i in range(3):
    p = Process(target=mp_worker, args=(f"Proc-{i+1}",))
    processes.append(p)
    p.start()
for p in processes:
    p.join()
print(f"共有リストの内容: {list(shared_list)}")
```

## 5. 非機能要件

* コードは可読性の高いコメント付きで記述すること
* Python標準ライブラリのみで動作可能（GPIOは例外）
* テストは自動実行スクリプトや手順書として提供すること

## 6. 開発環境・依存関係

* **Python**: 3.6以上
* **ライブラリ**:

  * threading（標準ライブラリ）
  * multiprocessing（標準ライブラリ）
  * (Raspberry Pi GPIO用) RPi.GPIOまたはgpiozero
* **ツール**: Git, GitHubアカウント

## 7. テスト要件

* 各サンプルコードを実行し、期待される出力と動作を確認する手順を記載すること
* テスト結果はREADMEに追記し、PRにて報告すること

## 8. ファイル作成とリポジトリ追加

* 指定されたファイル名で各サンプルコードを作成し、下記ファイル名で保存してください。

  * `semaphore_example.py`
  * `mutex_example.py`
  * `mp_semaphore_lock.py`
* 作成後は「7. テスト要件」に従い動作確認を実施し、正常動作を確認できたら以下の手順でリポジトリへ追加してください。

  1. `feature/add-samples` ブランチを作成
  2. ファイルをステージングしてコミット (`git add`、`git commit -m "Add sample code files"`)
  3. リモートへプッシュ (`git push origin feature/add-samples`)
  4. `main` ブランチへのPull Requestを作成し、動作確認結果を記載

## 8. GitHub運用要件

* ブランチ命名規則: `feature/<issue番号>-<短い説明>`
* コミットメッセージ: 変更点を明確に記載
* Pull Request: レビュー依頼と動作確認結果を添えて作成

## 9. 保守・運用要件

* 追加サンプルやバグ修正はIssue管理を行うこと
* ドキュメント更新時には必ずバージョンタグを付与すること

---

以上の要件を満たす形で、リポジトリへのコード追加およびドキュメント整備をお願いします。

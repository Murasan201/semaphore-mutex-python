# Semaphore and Mutex Examples in Python

This repository provides practical examples of using semaphores and mutexes for thread synchronization and process coordination in Python. These samples are designed to improve stability in multi-threaded and multi-process applications on Raspberry Pi and general Linux/Windows environments.

## Features

- **Semaphore Example**: Demonstrates resource access control with limited concurrent execution
- **Mutex Example**: Shows thread-safe counter updates using locks
- **Multiprocessing Example**: Illustrates process synchronization with shared resources

## Requirements

- Python 3.6 or higher
- Standard Python libraries only (no external dependencies)
- Compatible with:
  - Raspberry Pi OS
  - Ubuntu 22.04+
  - Windows 10/11
  - macOS

## Sample Files

### 1. `semaphore_example.py`
Demonstrates semaphore usage to limit concurrent access to resources.

**Key Features:**
- Limits simultaneous execution to 2 tasks
- Shows proper `acquire()` and `release()` patterns
- Demonstrates queuing behavior when resources are exhausted

**Usage:**
```bash
python3 semaphore_example.py
```

### 2. `mutex_example.py`
Shows mutex (lock) usage for thread-safe operations on shared data.

**Key Features:**
- Thread-safe counter incrementation
- Uses `with lock:` context manager for critical sections
- Demonstrates prevention of race conditions

**Usage:**
```bash
python3 mutex_example.py
```

### 3. `mp_semaphore_lock.py`
Illustrates multiprocessing synchronization with shared resources.

**Key Features:**
- Process-level semaphore and lock usage
- Shared list and dictionary examples
- Demonstrates inter-process communication safety

**Usage:**
```bash
python3 mp_semaphore_lock.py
```

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/Murasan201/semaphore-mutex-python.git
cd semaphore-mutex-python
```

2. Run any example:
```bash
python3 semaphore_example.py
python3 mutex_example.py
python3 mp_semaphore_lock.py
```

## Key Concepts

### Semaphore
A synchronization primitive that maintains a count of available resources. Useful when you need to limit the number of threads/processes that can access a resource simultaneously.

### Mutex (Mutual Exclusion)
A synchronization primitive that ensures only one thread can access a critical section at a time. Essential for preventing race conditions in shared data access.

### Process vs Thread Synchronization
- **Threading**: Shared memory space, lightweight, uses `threading.Lock()` and `threading.Semaphore()`
- **Multiprocessing**: Separate memory spaces, more robust, uses `multiprocessing.Lock()` and `multiprocessing.Semaphore()`

## Expected Output Examples

### Semaphore Example Output
```
Task-1 が実行待ち... アクセス権の取得を待機
Task-1 がリソースを使用中
Task-2 が実行待ち... アクセス権の取得を待機
Task-2 がリソースを使用中
...
すべてのタスクが完了しました
```

### Mutex Example Output
```
Thread-1 がロックの取得を試みています
Thread-1 がロック取得 (カウンター更新)
Thread-1 更新後のカウント: 1
...
最終カウント: 10
ミューテックスにより正しく10回インクリメントされました
```

## Use Cases

- **Web Servers**: Limiting concurrent connections
- **Database Access**: Controlling simultaneous database operations
- **File Processing**: Managing concurrent file operations
- **Resource Pools**: Connection pools, thread pools
- **IoT Applications**: Sensor data collection with rate limiting

## Best Practices

1. Always use context managers (`with lock:`) when possible
2. Keep critical sections as small as possible
3. Avoid nested locks to prevent deadlocks
4. Use timeouts for acquire operations in production code
5. Consider using `threading.RLock()` for reentrant scenarios

## Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Created as educational examples for understanding synchronization primitives in Python.

For more information, visit: https://murasan-net.com/
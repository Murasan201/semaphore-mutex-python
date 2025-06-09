# �v����`��: semaphore-mutex-python ���|�W�g��

**���|�W�g��URL**: [https://github.com/Murasan201/semaphore-mutex-python](https://github.com/Murasan201/semaphore-mutex-python)

## 1. �w�i�E�ړI

�{�v���W�F�N�g�́APython�ɂ�����Z�}�t�H�iSemaphore�j����у~���[�e�b�N�X�iMutex�j�𗘗p�����r������T���v���R�[�h��񋟂��ARaspberry Pi���ʓI��Linux/Windows���ł̃}���`�X���b�h�E�}���`�v���Z�X�����̈��萫������x�����܂��B

## 2. �K�p�͈�

* �ΏۃR�[�h: `semaphore_example.py`, `mutex_example.py`, `mp_semaphore_lock.py`
* ��: Python 3.6�ȏ�ARaspberry Pi OS�AUbuntu 22.04�ȏ�AWindows 10/11

## 3. �p���`

* **�Z�}�t�H (Semaphore)**: �����ɃA�N�Z�X�\�ȃ��\�[�X���𐧌����铯���@�\
* **�~���[�e�b�N�X (Mutex)**: ��x�Ɉ�̃^�X�N�݂̂��A�N�Z�X�\�Ȕr������@�\
* **�X���b�h (Thread)**: �v���Z�X���ŕ��s���s����鏈���P��
* **�v���Z�X (Process)**: OS����Ɨ��������s�P��

## 4. �@�\�v��

### 4.1 �Z�}�t�H����T���v��

* �������s����2�ɐ����ł��邱��
* `acquire()` �ɂ��ҋ@�A`release()` �ɂ�郊�\�[�X��������삷�邱��

#### �T���v���R�[�h: semaphore\_example.py

```python
import threading
import time

sem = threading.Semaphore(2)  # �������s��2�܂łɐ���

def worker(name):
    print(f"{name} �����s�҂�... �A�N�Z�X�����擾���܂�")
    sem.acquire()
    try:
        print(f"{name} �����\�[�X���g�p��")
        time.sleep(2)
    finally:
        print(f"{name} �����\�[�X�����")
        sem.release()

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(f"Task-{i+1}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
print("���ׂẴ^�X�N���������܂���")
```

### 4.2 �~���[�e�b�N�X����T���v��

* ���L�J�E���^���X���b�h�Ԃň��S�ɍX�V�ł��邱��
* `with lock` ��p�����N���e�B�J���Z�N�V���������������삷�邱��

#### �T���v���R�[�h: mutex\_example.py

```python
import threading
import time

lock = threading.Lock()
_shared_counter = 0  # ���L���\�[�X

def increment(name):
    global _shared_counter
    print(f"{name} �����b�N���擾���悤�Ƃ��Ă��܂�")
    with lock:
        print(f"{name} �����b�N�擾 (�J�E���g���X�V)")
        val = _shared_counter
        time.sleep(0.5)  # �Ӑ}�I�ȏ����x��
        _shared_counter = val + 1
        print(f"{name} �X�V��̃J�E���g: {_shared_counter}")

threads = []
for i in range(10):
    t = threading.Thread(target=increment, args=(f"Thread-{i+1}",))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print(f"�ŏI�J�E���g: {_shared_counter}")
```

### 4.3 �}���`�v���Z�X����T���v��

* �v���Z�X�Ԃŋ��L�\�ȃ��X�g�ɐ������v�f�ǉ��ł��邱��
* `Semaphore(1)` �ɂ��v���Z�X�P�ʂ̔r�����䂪���삷�邱��

#### �T���v���R�[�h: mp\_semaphore\_lock.py

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
        print(f"{name} �����X�g�ɒǉ���")
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
print(f"���L���X�g�̓��e: {list(shared_list)}")
```

## 5. ��@�\�v��

* �R�[�h�͉ǐ��̍����R�����g�t���ŋL�q���邱��
* Python�W�����C�u�����݂̂œ���\�iGPIO�͗�O�j
* �e�X�g�͎������s�X�N���v�g��菇���Ƃ��Ē񋟂��邱��

## 6. �J�����E�ˑ��֌W

* **Python**: 3.6�ȏ�
* **���C�u����**:

  * threading�i�W�����C�u�����j
  * multiprocessing�i�W�����C�u�����j
  * (Raspberry Pi GPIO�p) RPi.GPIO�܂���gpiozero
* **�c�[��**: Git, GitHub�A�J�E���g

## 7. �e�X�g�v��

* �e�T���v���R�[�h�����s���A���҂����o�͂Ɠ�����m�F����菇���L�ڂ��邱��
* �e�X�g���ʂ�README�ɒǋL���APR�ɂĕ񍐂��邱��

## 8. �t�@�C���쐬�ƃ��|�W�g���ǉ�

* �w�肳�ꂽ�t�@�C�����Ŋe�T���v���R�[�h���쐬���A���L�t�@�C�����ŕۑ����Ă��������B

  * `semaphore_example.py`
  * `mutex_example.py`
  * `mp_semaphore_lock.py`
* �쐬��́u7. �e�X�g�v���v�ɏ]������m�F�����{���A���퓮����m�F�ł�����ȉ��̎菇�Ń��|�W�g���֒ǉ����Ă��������B

  1. `feature/add-samples` �u�����`���쐬
  2. �t�@�C�����X�e�[�W���O���ăR�~�b�g (`git add`�A`git commit -m "Add sample code files"`)
  3. �����[�g�փv�b�V�� (`git push origin feature/add-samples`)
  4. `main` �u�����`�ւ�Pull Request���쐬���A����m�F���ʂ��L��

## 8. GitHub�^�p�v��

* �u�����`�����K��: `feature/<issue�ԍ�>-<�Z������>`
* �R�~�b�g���b�Z�[�W: �ύX�_�𖾊m�ɋL��
* Pull Request: ���r���[�˗��Ɠ���m�F���ʂ�Y���č쐬

## 9. �ێ�E�^�p�v��

* �ǉ��T���v����o�O�C����Issue�Ǘ����s������
* �h�L�������g�X�V���ɂ͕K���o�[�W�����^�O��t�^���邱��

---

�ȏ�̗v���𖞂����`�ŁA���|�W�g���ւ̃R�[�h�ǉ�����уh�L�������g���������肢���܂��B

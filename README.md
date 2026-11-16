# Threads and Multithreading Laboratory

## Student Information

- Name: RHEA LEEN P. CASTOR
- Section: BSCA-3
- Date: November 16, 2026

## Laboratory Description

This lab uses Python to create and run threads, coordinate tasks with join(), and protect a shared counter with Lock().

## Completed Tasks

1. Single Thread
2. Multiple Threads
3. Thread Synchronization using join()
4. Shared Resource Management using Lock()

Run each program from the repository folder.

```bash
python3 task1_single_thread.py
python3 task2_multiple_threads.py
python3 task3_thread_synchronization.py
python3 task4_thread_lock.py
```

| Task | Observed result |
| --- | --- |
| Single Thread | Printed numbers 1 to 5, then Program completed. |
| Multiple Threads | Both workers printed numbers 1 to 5, then Both threads completed. The run took about 5 seconds. |
| Thread Synchronization | Download completed. appeared before Main program continues. when join() was used. |
| Thread Lock | The locked counter ended at 200000. |

Without join(), Main program continues. appeared before Download completed. The worker still finished before the process exited.

All five no-lock counter trials also ended at 200000 on CPython 3.12.14 with the GIL enabled. These trials did not show a lost update. The final program uses the lock to protect the counter update.

## Learning Outcomes

- Create and start threads.
- Explain how concurrent tasks make progress.
- Use join() to wait for a worker to finish.
- Use a lock to protect a shared counter.

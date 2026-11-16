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

## Execution Screenshots

| Execution | Evidence |
| --- | --- |
| Task 1 single thread | [Screenshot](screenshots/01_task1_single_thread.jpg) |
| Task 2 multiple threads | [Screenshot](screenshots/02_task2_multiple_threads.jpg) |
| Task 3 with join() | [Screenshot](screenshots/03_task3_with_join.jpg) |
| Task 3 without join() | [Screenshot](screenshots/04_task3_without_join.jpg) |
| Task 4 with the lock | [Screenshot](screenshots/05_task4_with_lock.jpg) |
| Task 4 without the lock, five trials | [Screenshot](screenshots/06_task4_without_lock.jpg) |

## Guide Questions

### Task 1

1. **What is the purpose of threading.Thread()?**

   threading.Thread() creates a thread object and assigns the function that it will run.

2. **What happens when start() is executed?**

   start() begins the new thread and runs its target function.

3. **What is the purpose of join()?**

   join() makes the calling thread wait until the other thread finishes.

4. **What happens if join() is removed?**

   The main thread can print Program completed. while the worker is still displaying numbers. The process stays open until the non-daemon worker finishes.


### Task 2

1. **How many threads are created in the program?**

   The program creates two worker threads. The main thread also exists.

2. **Do the two threads execute independently?**

   Yes. Each worker runs its own loop, while both share the same process.

3. **Why might the output order change when the program is executed again?**

   The operating system may give the threads CPU time in a different order on each run.

4. **What is the difference between sequential and concurrent execution?**

   Sequential execution finishes one task before starting the next. Concurrent execution allows tasks to make progress during the same time period.


### Task 3

1. **Why does the main program wait when join() is used?**

   join() pauses the main thread until the download thread has finished.

2. **What happens when join() is removed?**

   In the test, Main program continues. appeared before Download completed. The main thread continued early, while the process stayed open until the non-daemon download thread finished.

3. **In what situations is thread synchronization necessary?**

   Synchronization is needed when one task must wait for another result or when threads change shared data.


### Task 4

1. **What is a shared resource?**

   A shared resource is data or an object used by more than one thread, such as the counter variable.

2. **What is a race condition?**

   A race condition happens when the result depends on how the operations of different threads overlap. Two counter updates can interfere and lose an increment.

3. **What is the purpose of threading.Lock()?**

   threading.Lock() allows one thread at a time to enter the protected section.

4. **What is a critical section?**

   A critical section is the part of the code that accesses shared data and needs protection from interfering operations.

5. **Why is synchronization important when multiple threads access shared data?**

   Synchronization controls access to shared data so thread operations do not interfere. The locked run reached 200000. All five unlocked trials also reached 200000 in this environment, so these trials did not show a lost update.


### General Questions

1. **What is the difference between a process and a thread?**

   A process is a running program with its own memory space. A thread is an execution path inside a process and shares that process’s memory with its other threads.

2. **What are the advantages of using multithreading?**

   Multithreading can keep a program responsive and allow useful work while another task waits for input or output. Threads also share data within one process.

3. **How does multithreading improve application responsiveness?**

   A worker thread can handle a slow task while the main thread continues handling the interface or other work.

4. **What is the difference between concurrency and parallelism?**

   Concurrency means tasks make progress during the same time period. Parallelism means tasks execute at the same instant on different CPU execution units.

5. **Why is a lock necessary when multiple threads access shared data?**

   A lock is needed when simultaneous changes to shared data could interfere. It lets one thread finish the protected operation before another enters.

6. **What might happen if a thread is not properly synchronized?**

   Operations may happen in the wrong order, data may become incorrect, or the main thread may use a result before it is ready.

7. **Can multiple threads execute simultaneously on a single-core processor? Explain.**

   In the usual single-core scheduling model, one thread executes at a time. The operating system switches between threads, so they run concurrently.

8. **How does the operating system manage kernel-level threads?**

   The operating system schedules kernel-level threads, assigns CPU time, and saves and restores each thread’s CPU state during a switch. It also tracks whether a thread is ready, running, or waiting.

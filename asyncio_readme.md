 `asyncio` functions and classes in a tree format with examples directly underneath each item for clarity.

```python
asyncio
│
├── run()
│   └── Example:
│       import asyncio
│       
│       async def say_hello():
│           print("Hello, World!")
│       
│       asyncio.run(say_hello())
│
├── gather()
│   └── Example:
│       import asyncio
│       
│       async def task1():
│           await asyncio.sleep(1)
│           print("Task 1 Complete")
│       
│       async def task2():
│           await asyncio.sleep(2)
│           print("Task 2 Complete")
│       
│       async def main():
│           await asyncio.gather(task1(), task2())
│       
│       asyncio.run(main())
│
├── sleep()
│   └── Example:
│       import asyncio
│       
│       async def pause():
│           print("Sleeping for 2 seconds...")
│           await asyncio.sleep(2)
│           print("Awake!")
│       
│       asyncio.run(pause())
│
├── create_task()
│   └── Example:
│       import asyncio
│       
│       async def do_work():
│           print("Working...")
│           await asyncio.sleep(1)
│           print("Work done!")
│       
│       async def main():
│           task = asyncio.create_task(do_work())
│           await task
│       
│       asyncio.run(main())
│
├── get_event_loop()
│   └── Example:
│       import asyncio
│       
│       async def example():
│           loop = asyncio.get_event_loop()
│           print(f"Current event loop: {loop}")
│       
│       asyncio.run(example())
│
├── new_event_loop()
│   └── Example:
│       import asyncio
│       
│       # Create a new event loop
│       loop = asyncio.new_event_loop()
│       asyncio.set_event_loop(loop)
│       
│       async def example():
│           print("Using a new event loop")
│       
│       loop.run_until_complete(example())
│       loop.close()
│
├── wait()
│   └── Example:
│       import asyncio
│       
│       async def task1():
│           await asyncio.sleep(1)
│           print("Task 1 Complete")
│       
│       async def task2():
│           await asyncio.sleep(2)
│           print("Task 2 Complete")
│       
│       async def main():
│           done, pending = await asyncio.wait([task1(), task2()])
│           for task in done:
│               print(f"{task} is done")
│       
│       asyncio.run(main())
│
├── Future
│   └── Example:
│       import asyncio
│       
│       async def set_future_value(future):
│           await asyncio.sleep(1)
│           future.set_result("Future result")
│       
│       async def main():
│           future = asyncio.Future()
│           await asyncio.gather(set_future_value(future))
│           print(f"Future result: {future.result()}")
│       
│       asyncio.run(main())
│
└── Task
    └── Example:
        import asyncio
        
        async def do_work():
            await asyncio.sleep(1)
            print("Task finished!")
        
        async def main():
            task = asyncio.create_task(do_work())
            await task
        
        asyncio.run(main())
```


## Examples

### `asyncio.run()`
Starts the event loop and runs a specified coroutine.

```python
import asyncio

async def say_hello():
    print("Hello, World!")

asyncio.run(say_hello())
```

### `asyncio.gather()`
Runs multiple coroutines concurrently and waits for them to complete.

```python
import asyncio

async def task1():
    await asyncio.sleep(1)
    print("Task 1 Complete")

async def task2():
    await asyncio.sleep(2)
    print("Task 2 Complete")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())
```

### `asyncio.sleep()`
Asynchronously sleeps for the specified time without blocking the event loop.

```python
import asyncio

async def pause():
    print("Sleeping for 2 seconds...")
    await asyncio.sleep(2)
    print("Awake!")

asyncio.run(pause())
```

### `asyncio.create_task()`
Schedules a coroutine to be run in the event loop as a Task.

```python
import asyncio

async def do_work():
    print("Working...")
    await asyncio.sleep(1)
    print("Work done!")

async def main():
    task = asyncio.create_task(do_work())
    await task

asyncio.run(main())
```

### `asyncio.get_event_loop()`
Retrieves the current event loop object.

```python
import asyncio

async def example():
    loop = asyncio.get_event_loop()
    print(f"Current event loop: {loop}")

asyncio.run(example())
```

### `asyncio.new_event_loop()`
Creates a new event loop object.

```python
import asyncio

# Create a new event loop
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

async def example():
    print("Using a new event loop")

loop.run_until_complete(example())
loop.close()
```

### `asyncio.wait()`
Waits for a set of Futures or coroutines to complete.

```python
import asyncio

async def task1():
    await asyncio.sleep(1)
    print("Task 1 Complete")

async def task2():
    await asyncio.sleep(2)
    print("Task 2 Complete")

async def main():
    done, pending = await asyncio.wait([task1(), task2()])
    for task in done:
        print(f"{task} is done")

asyncio.run(main())
```

### `asyncio.Future`
A low-level object that represents an eventual result of an asynchronous operation. It's often used internally.

```python
import asyncio

async def set_future_value(future):
    await asyncio.sleep(1)
    future.set_result("Future result")

async def main():
    future = asyncio.Future()
    await asyncio.gather(set_future_value(future))
    print(f"Future result: {future.result()}")

asyncio.run(main())
```

### `asyncio.Task`
A subclass of Future that is used to schedule coroutines to run on the event loop.

```python
import asyncio

async def do_work():
    await asyncio.sleep(1)
    print("Task finished!")

async def main():
    task = asyncio.create_task(do_work())
    await task

asyncio.run(main())
```

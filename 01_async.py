import asyncio
import time

# async def say_hello():
#     print("Hello")




# asyncio.run(main())

# async def say_hello():
#     """
#     Asynchronous function that prints "Hello", waits for 1 second, 
#     and then prints "world".

#     This function demonstrates the use of asyncio.sleep to pause 
#     execution and allow other tasks to run concurrently during the wait.

#     Returns:
#         None
#     """
#     print("Hello")
#     await asyncio.sleep(1) # "wait here for 1 second before continuing.
#     # "During this pause, the event loop can run other tasks if they are available. This is how you achieve concurrency.
#     print("world")

# # Directly use await in interactive environments like Jupyter Notebook
# async def main():
#     await say_hello()


# asyncio.run(main())


## Normal Version

def BrewCoffee():
    print("Brewing coffee...")
    time.sleep(3)
    print("coffee brewed...")
    return "coffee ready"


def ToastBread():
    print("Toasting Bread...")
    time.sleep(2)
    print("Toasting Done.")
    return "bread toasted"

def main():

    start = time.time()
    BrewCoffee()
    ToastBread()
    end = time.time()

    print(f"time required :{end - start} secs ")

if __name__ == "__main__":
    main()


# asynchronous version
async def BrewCoffee():
    print("Brewing coffee...")
    await asyncio.sleep(3)
    print("coffee brewed...")
    return "coffee ready"


async def ToastBread():
    print("Toasting Bread...")
    await asyncio.sleep(2)
    print("Toasting Done.")
    return "bread toasted"

async def main():

    start = time.time()
    batch = asyncio.gather(BrewCoffee(), ToastBread())
    coffee, toast = await batch
    end = time.time()

    print(f"time required :{end - start} secs ")

if __name__ == "__main__":
    asyncio.run(main())


# asynchronous version
async def BrewCoffee():
    print("Brewing coffee...")
    await asyncio.sleep(3)
    print("coffee brewed...")
    return "coffee ready"


async def ToastBread():
    print("Toasting Bread...")
    await asyncio.sleep(2)
    print("Toasting Done.")
    return "bread toasted"

async def main2():

    start = time.time()
    coffee_task = asyncio.create_task(BrewCoffee())
    toast_task = asyncio.create_task(ToastBread())

    result_coffee = await coffee_task
    result_toast = await toast_task
    
    end = time.time()

    print(f"time required :{end - start} secs ")

if __name__ == "__main__":
    asyncio.run(main())




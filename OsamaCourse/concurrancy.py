import time
import asyncio
startTime=time.time()

# for i in range(1000000):
#     continue
    
# EndTime=time.time()
# print(EndTime-startTime)

async def order(order_type,duration):
    print(f'{order_type} request start')
    await asyncio.sleep(duration)
    print(f'{order_type} request End')


async def main():
    task1=asyncio.create_task( order("tea",5))
    task2=asyncio.create_task( order("coffee",1))
    task3=asyncio.create_task( order("milk",2))
    await task1
    await task2
    await task3

asyncio.run(main())
EndTime=time.time()
print(int(EndTime-startTime))
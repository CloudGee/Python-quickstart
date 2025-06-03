# # async, await
# import asyncio

# async def cook_rice():
#     print("开始煮米饭")
#     # 同步方式：sleep(3)
#     await asyncio.sleep(3)  # 等待3秒
#     print("米饭煮好了")
#     return "米饭"

# async def cook_soup():
#     print("开始煮汤")
#     await asyncio.sleep(2)  # 等待2秒
#     print("汤煮好了")
#     return "汤"

# async def prepare_meal():
#     print("开始准备晚餐")

#     # 串行执行 - 总共5秒
#     # rice = await cook_rice()    # 等待3秒
#     # soup = await cook_soup()    # 等待2秒

#     # 并行执行 - 总共3秒（最长的任务时间）
#     rice_task = asyncio.create_task(cook_rice())
#     soup_task = asyncio.create_task(cook_soup())

#     rice = await rice_task
#     soup = await soup_task

#     print(f"晚餐准备完成: {rice} + {soup}")

# asyncio.run(prepare_meal())

# import asyncio
# async def task(N):
#   await asyncio.sleep(N)
#   print(f"任务{N}完成")

# async def main():
#   # await asyncio.gather(task(1), task(2), task(3))
#   # await asyncio.gather(*(task(i) for i in range(1,4)))

# asyncio.run(main())

# async for
import asyncio

async def async_range(n):
    for i in range(1, n + 1):
        await asyncio.sleep(2)  # 模拟异步操作
        yield i

async def main():
    async for i in async_range(3):
        print(f"值: {i}")

asyncio.run(main())
# <2 seconds later>
# 值: 1
# <2 seconds later>
# 值: 2
# <2 seconds later>
# 值: 3
# async for 其实就是对异步迭代器的支持，类似于普通的 for 循环，但它允许在迭代过程中使用 await 关键字来等待异步操作完成。
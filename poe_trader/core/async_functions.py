import asyncio
from functools import partial
from concurrent.futures import ProcessPoolExecutor

def process_async_data(fn, list_of_arg_tuples):
    loop, executor = get_loop_and_executor(len(list_of_arg_tuples))
    tasks = [asyncio.ensure_future(loop.run_in_executor(executor, partial(fn, *args)))
             for args in list_of_arg_tuples]
    run_tasks_then_close_loop(loop, tasks)

def get_loop_and_executor(executor_size):
    loop = asyncio.get_event_loop()
    executor = ProcessPoolExecutor(executor_size)
    return loop, executor


def run_tasks_then_close_loop(loop, tasks):
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
import asyncio

class AsyncTaskManager:
    def __init__(self, max_concurrent_tasks=10):
        self.semaphore = asyncio.Semaphore(max_concurrent_tasks)
        self.tasks = []

    async def add_task(self, coro):
        """Add a task to the task list, ensuring it respects the semaphore."""
        async def task_with_semaphore():
            async with self.semaphore:
                return await coro

        task = asyncio.create_task(task_with_semaphore())
        self.tasks.append(task)

    async def get_all_results(self):
        """Wait for all tasks to complete and return their results."""
        return await asyncio.gather(*self.tasks)
    

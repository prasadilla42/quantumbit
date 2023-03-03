import asyncio


class System:
    def __init__(self, runtimes):
        self.runtimes = runtimes
        self.loop = asyncio.get_event_loop()

    async def choose_best_runtime(self):
        best_runtime = None
        best_score = float('-inf')

        for runtime in self.runtimes:
            capacity = await runtime.get_capacity()
            latency = await runtime.get_latency()
            availability = await runtime.get_availability()

            score = capacity / (latency * availability)

            if score > best_score:
                best_score = score
                best_runtime = runtime

        return best_runtime

    async def do_something_async(self, command):
        runtime = await self.choose_best_runtime()
        result = await runtime.execute_command(command, RuntimeType.VERBATIM)

        return result

    def do_something(self, command):
        return self.loop.run_until_complete(self.do_something_async(command))

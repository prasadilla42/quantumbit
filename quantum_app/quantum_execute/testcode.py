import asyncio
from enum import Enum


class RuntimeType(Enum):
    VERBATIM = 1
    SIMULATION = 2
    ECHO = 3
    NEW_RUNTIME_1 = 4
    NEW_RUNTIME_2 = 5
    # ...


class IRuntime:
    async def connect(self):
        pass

    async def disconnect(self):
        pass

    async def get_capacity(self):
        pass

    async def get_latency(self):
        pass

    async def get_availability(self):
        pass

    async def execute_command(self, command, runtime_type):
        pass


class VerbatimRuntime(IRuntime):
    async def connect(self):
        pass

    async def disconnect(self):
        pass

    async def get_capacity(self):
        return 1.0

    async def get_latency(self):
        return 0.1

    async def get_availability(self):
        return 1.0

    async def execute_command(self, command, runtime_type):
        # execute the command in verbatim mode
        pass


class SimulationRuntime(IRuntime):
    async def connect(self):
        pass

    async def disconnect(self):
        pass

    async def get_capacity(self):
        return 0.5

    async def get_latency(self):
        return 0.2

    async def get_availability(self):
        return 0.9

    async def execute_command(self, command, runtime_type):
        # simulate the execution of the command
        pass


class EchoRuntime(IRuntime):
    async def connect(self):
        pass

    async def disconnect(self):
        pass

    async def get_capacity(self):
        return 0.2

    async def get_latency(self):
        return 0.05

    async def get_availability(self):
        return 1.0

    async def execute_command(self, command, runtime_type):
        # return a fake result without actually executing the command
        return "fake_result"


class NewRuntime1(IRuntime):
    async def connect(self):
        pass

    async def disconnect(self):
        pass

    async def get_capacity(self):
        return 0.8

    async def get_latency(self):
        return 0.3

    async def get_availability(self):
        return 0.95

    async def execute_command(self, command, runtime_type):
        # execute the command using the new runtime 1
        pass


class NewRuntime2(IRuntime):
    async def connect(self):
        pass

    async def disconnect(self):
        pass

    async def get_capacity(self):
        return 0.6

    async def get_latency(self):
        return 0.4

    async def get_availability(self):
        return 0.9

    async def execute_command(self, command, runtime_type):
        # execute the command using the new runtime 2
        pass


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

    async def do_something_async(self, command, runtime_type):
        runtime = await self.choose_best_runtime()
        result = await runtime.execute

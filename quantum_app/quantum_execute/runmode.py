import asyncio
from enum import Enum

class RuntimeMode(Enum):
    VERBATIM = 1
    SIMULATION = 2
    ECHO = 3

class IRuntime:
    async def connect(self):
        pass

    async def disconnect(self):
        pass

    async def execute_command(self, command):
        pass

class VerbatimRuntime(IRuntime):
    async def connect(self):
        # Code to connect to the actual hardware-connected runtime
        return True

    async def disconnect(self):
        # Code to disconnect from the actual hardware-connected runtime
        return True

    async def execute_command(self, command):
        # Code to execute the command on the actual hardware-connected runtime
        return 0

class SimulationRuntime(IRuntime):
    async def connect(self):
        # Code to connect to the simulator
        return True

    async def disconnect(self):
        # Code to disconnect from the simulator
        return True

    async def execute_command(self, command):
        # Code to simulate the execution of the command
        return 0

class EchoRuntime(IRuntime):
    async def connect(self):
        # Code to fake the connection
        return True

    async def disconnect(self):
        # Code to fake the disconnection
        return True

    async def execute_command(self, command):
        # Code to fake the return code
        return 0

class System:
    def __init__(self, mode):
        self.mode = mode
        self.loop = asyncio.get_event_loop()

    async def do_something_async(self):
        if self.mode == RuntimeMode.VERBATIM:
            runtime = VerbatimRuntime()
        elif self.mode == RuntimeMode.SIMULATION:
            runtime = SimulationRuntime()
        elif self.mode == RuntimeMode.ECHO:
            runtime = EchoRuntime()
        else:
            raise ValueError("Invalid runtime mode: {}".format(self.mode))

        await runtime.connect()
        # Code that uses the runtime asynchronously
        result = await runtime.execute_command("some_command")
        await runtime.disconnect()

        return result

    def do_something(self):
        return self.loop.run_until_complete(self.do_something_async())

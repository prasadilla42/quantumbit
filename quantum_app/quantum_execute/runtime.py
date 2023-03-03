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

import asyncio
from rest_framework.views import APIView
from rest_framework.response import Response

class AsyncExampleView(APIView):
    async def get(self, request):
        # Simulate an async I/O operation
        result = await self.perform_heavy_task()
        return Response({'result': result})

    async def perform_heavy_task(self):
        # Simulate a time-consuming operation
        await asyncio.sleep(2)
        return "heavy async result"
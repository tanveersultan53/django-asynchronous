import time
from django.utils.deprecation import MiddlewareMixin


class AsyncLoggingMiddleware(MiddlewareMixin):
    async def __call__(self, request):
        start_time = time.time()

        # Process the request
        response = await self.get_response(request)

        # Calculate the duration and log it
        duration = time.time() - start_time
        print(f"Request took {duration:.2f} seconds")

        return response
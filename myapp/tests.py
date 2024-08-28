from django.test import AsyncClient, TestCase

class AsyncViewTests(TestCase):
    async def test_async_view(self):
        client = AsyncClient()
        response = await client.get('/async-view/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'result': 'heavy async result'})
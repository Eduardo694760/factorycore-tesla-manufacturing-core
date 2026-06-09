import httpx
import asyncio

async def main():
    async with httpx.AsyncClient(base_url="http://127.0.0.1:8000") as client:
        r = await client.get("/operadores")
        print("Operadores:", r.json())

        r = await client.get("/maquinas")
        print("Máquinas:", r.json())

        r = await client.get("/lotes")
        print("Lotes:", r.json())

if __name__ == "__main__":
    asyncio.run(main())


import asyncio
import edge_tts

async def test_types():
    try:
        comm = edge_tts.Communicate("Hello world test", "en-US-JennyNeural")
        async for c in comm.stream():
            print(f"Type: {c['type']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(test_types())

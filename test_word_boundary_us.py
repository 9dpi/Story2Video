import asyncio
import edge_tts

async def test_sub_data():
    try:
        comm = edge_tts.Communicate("Hello world", "en-US-JennyNeural")
        async for c in comm.stream():
            if c["type"] == "WordBoundary":
                print(c)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(test_sub_data())

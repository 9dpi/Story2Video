import asyncio
import edge_tts

async def test_word_boundary():
    try:
        print("Testing with boundary='WordBoundary'...")
        comm = edge_tts.Communicate("Hello world", "en-US-JennyNeural", boundary="WordBoundary")
        async for c in comm.stream():
            if c["type"] == "WordBoundary":
                print(f"Word found: {c['text']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(test_word_boundary())

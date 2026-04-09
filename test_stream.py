import asyncio
import edge_tts

async def test_stream():
    try:
        print("Starting stream test...")
        comm = edge_tts.Communicate("Thử nghiệm luồng dữ liệu", "vi-VN-HoaiMyNeural")
        chunks = 0
        async for c in comm.stream():
            chunks += 1
        print(f"Success! Received {chunks} chunks.")
    except Exception as e:
        print(f"Stream test failed: {e}")

if __name__ == "__main__":
    asyncio.run(test_stream())

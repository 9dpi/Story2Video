import asyncio
import edge_tts

async def test_sub_data():
    try:
        comm = edge_tts.Communicate("Thử nghiệm phụ đề", "vi-VN-HoaiMyNeural")
        async for c in comm.stream():
            if c["type"] == "WordBoundary":
                print(f"Word: {c['text']} | Offset: {c['offset']} | Duration: {c['duration']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(test_sub_data())

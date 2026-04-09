import asyncio
import edge_tts

async def test_minimal():
    try:
        # Try US voice first (we know it worked before)
        print("Testing US Jenny...")
        c1 = edge_tts.Communicate("Hello", "en-US-JennyNeural")
        async for _ in c1.stream(): pass
        print("US Jenny OK")
        
        # Try VN Hoai My
        print("Testing VN Hoai My...")
        c2 = edge_tts.Communicate("Hello", "vi-VN-HoaiMyNeural")
        async for _ in c2.stream(): pass
        print("VN Hoai My OK")
        
    except Exception as e:
        print(f"FAILED: {e}")

if __name__ == "__main__":
    asyncio.run(test_minimal())

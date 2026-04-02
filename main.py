from google import genai
from PIL import ImageGrab
import time
import os

# --- CONFIGURATION ---
# Replace with your actual API key
API_KEY = "Your API Key Here" 
MODEL_ID = "gemini-2.0-flash" # The newest, fastest model
REGION = (0, 0, 1370, 900) #Enter your region from the top left as 0, 0

# don't touch unless you know what you're doing.
# A version with more reminders will be dropping soon or it is already there so check it out under main-more.py
client = genai.Client(api_key=API_KEY)

def capture_and_analyze():
    print(f"[{time.strftime('%H:%M:%S')}] Capturing screen...")
    
    # 1. Capture and save
    screenshot = ImageGrab.grab(bbox=REGION)
    screenshot.save("temp_capture.png")

    print("Analyzing with Gemini 2.0...")
    
    try:
        # 2. Use the types.Part helper to send the image correctly
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=[
                types.Part.from_bytes(
                    data=open("temp_capture.png", "rb").read(),
                    mime_type="image/png"
                ),
                "Describe what is happening in this image briefly."
            ]
        )
        
        print("\n--- AI ANALYSIS ---")
        print(response.text)
        print("-------------------\n")

    except Exception as e:
        print(f"Error: {e}")
        
        print("\n--- AI ANALYSIS ---")
        print(response.text)
        print("-------------------\n")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Modern Assistant Started. Press Ctrl+C to stop.")
    try:
        while True:
            capture_and_analyze()
            time.sleep(45)
    except KeyboardInterrupt:
        print("\nStopped by user.")

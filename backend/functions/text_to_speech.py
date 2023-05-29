import requests

from decouple import config

ELEVEN_LABS_API_KEY = config("ELEVEN_LABS_API_KEY")

# Eleven Labs
# Convert Text to Speech


def convert_text_to_speech(message):

    # Define Data (Body)
    body = {
        "text": message,
        "voice_settings": {
            "stability": 0,
            "similarity_boost": 0
        }
    }

    # Define voice
    voice_rachel = "21m00Tcm4TlvDq8ikWAM"

    # All voices
    # ...
    # voice_rachel = "21m00Tcm4TlvDq8ikWAM"
    # voice_domi = "AZnzlk1XvdvUeBnXmlld"
    # voice_bella = "EXAVITQu4vr4xnSDxMaL"
    # voice_antoni = "ErXwobaYiN019PkySvjV"
    # voice_antoni = "ErXwobaYiN019PkySvjV"
    # voice_elli = "MF3mGyEYCl7XYWbV9V6O"
    # voice_josh = "TxGEqnHWrfWFTfGW9XjX"
    # voice_arnold = "VR6AewLTigWG4xSOukaG"
    # voice_adam = "pNInz6obpgDQGcFmaJgB"
    # voice_sam = "yoZ06aMxZJJ28mfd3POQ"

    # Constructing Headers and Endpoint
    headers = {"xi-api-key": ELEVEN_LABS_API_KEY,
               "Content-Type": "application/json", "accept": "audio/mpeg"}
    endpoint = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_rachel}"

    # Send Request
    try:
        response = requests.post(endpoint, json=body, headers=headers)
    except Exception as e:
        return

    # Handle Response
    if response.status_code == 200:
        return response.content
    else:
        return

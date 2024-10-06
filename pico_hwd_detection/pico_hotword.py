# hotword_detector.py

import struct
import pyaudio
import pvporcupine
from colorama import Fore, Style


def hotword_detection(access_key):
    """
    Detects hotwords using Picovoice Porcupine.

    Args:
        access_key (str): The access key for the Picovoice API.
    """
    porcupine = None
    paud = None
    audio_stream = None

    try:
        porcupine = pvporcupine.create(access_key=access_key, keywords=["jarvis", "jarvis"])
        paud = pyaudio.PyAudio()
        audio_stream = paud.open(rate=porcupine.sample_rate,
                                  channels=1,
                                  format=pyaudio.paInt16,
                                  input=True,
                                  frames_per_buffer=porcupine.frame_length)
        print(Fore.CYAN +"Listening for hotword..."+Style.RESET_ALL)  # Optional: A message to indicate listening has started
        while True:
            keyword = audio_stream.read(porcupine.frame_length)
            keyword = struct.unpack_from("h" * porcupine.frame_length, keyword)
            keyword_index = porcupine.process(keyword)
            if keyword_index >= 0:
                print(Fore.GREEN + "Hotword Detected" + Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}" + Style.RESET_ALL)

    finally:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()


# Example usage: Uncomment the line below to test the function directly.


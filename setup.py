from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.1'
DESCRIPTION = 'Hotword Detection with Porcupine and Python'
LONG_DESCRIPTION =  """# Hotword Detection with Porcupine

In the realm of modern technology, voice-controlled applications have emerged as an integral component of our digital landscape. Propelled by the widespread adoption of virtual assistants such as Jarvis, Siri, and Alexa, users have become accustomed to seamless interactions with their devices through spoken commands. At the core of these sophisticated applications lies a critical functionality — Hotword detection. This essential feature serves as the catalyst, prompting the system to actively listen and respond, creating a dynamic and intuitive user experience.

## Overview

This Python module provides a lightweight and efficient solution for implementing hotword detection using the Porcupine library developed by Picovoice. Designed for real-time performance, this module enables developers to easily integrate voice-triggered commands into their applications, enhancing user engagement and accessibility.

## Key Features

- **Real-time Hotword Detection**: The module utilizes the Porcupine engine to detect predefined hotwords with minimal latency, ensuring prompt response times.
- **Customizable Keywords**: Users can easily modify the list of hotwords based on their application requirements.
- **Cross-Platform Compatibility**: Works seamlessly on various platforms, making it suitable for desktop and embedded applications alike.
- **User-Friendly API**: Simple and intuitive functions for easy integration into existing projects.

## Technical Details

The core functionality is encapsulated in the `hotword_detection` function, which leverages the Picovoice Porcupine API. The function initializes the Porcupine engine, listens for audio input, and processes it to detect specified hotwords.

### Example Usage

To utilize the hotword detection capabilities, simply call the `hotword_detection` function with your Picovoice access key:

```python
from hotword_detector import hotword_detection

# Replace 'your_access_key' with your actual Picovoice access key.
hotword_detection('your_access_key')
"""
# Setting up
setup(
    name="pico_hwd_detection",
    version=VERSION,
    author="Rohit Kumar Yadav",
    author_email="<rohitkuyadav2003@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    license="MIT",  # Add the license type here
    license_files=("LICENSE",), 
    install_requires=['PyAudio', 'pvporcupine', 'colorama'],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
    ]
)
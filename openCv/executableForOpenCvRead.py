from cx_Freeze import setup, Executable

setup(name = "Take_Vid_And_Record",
      version = "0.1",
      description = "Takes video from webcam and records it in you folder",
      executables = [Executable("videoReading.py")])

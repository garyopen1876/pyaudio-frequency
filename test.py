import numpy as np
import pyaudio

# 剛剛的正弦波取樣function
def sine(frequency= 3, time= 10, amplitude= 1, theta= 0, sample_rate=44100):   

    arange_time = np.arange(0, time, 1/sample_rate)
    
    return amplitude * np.sin(2 * np.pi * frequency * arange_time + theta)

# pyaudio的讀取方法
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,channels=1, rate=44100, output=True)

data =  sine(frequency= 500, time= 3, amplitude= 1, theta= 0, sample_rate=44100)
stream.write(data.astype(np.float32).tobytes())
stream.stop_stream()
stream.close()
p.terminate()



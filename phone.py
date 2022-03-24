from tkinter import *
import numpy as np
import pyaudio


def sine(frequency, time, sample_rate):   

    arange_time = np.arange(0, time, 1/sample_rate)
    amplitude = 1
    theta = 0
    return amplitude * np.sin(2 * np.pi * frequency * arange_time + theta)
 
 
def two_sine(f1, f2):
    time =  0.3
    sample_rate = 44100
    s1 = sine(f1, time, sample_rate)
    s2 = sine(f2, time, sample_rate)
    ss = s1+s2
    sa=np.divide(ss, 2)
    return sa
 
def play(f1, f2):
    data = two_sine(f1, f2)
    stream.write(data.astype(np.float32).tobytes())
    

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,channels=1, rate=44100, output=True)

# 手機模擬視窗
win = Tk()
win.title('電話模擬')
win.geometry('300x400') 
win.resizable(False, False)


# Button 
btn1 = Button(win, text='1', height = 5, width = 13, command=lambda: play(1209, 697))
btn1.grid(column=0, row=0, sticky='nesw')

btn2 = Button(win, text='2', height = 5, width = 13, command=lambda: play(1336, 697))
btn2.grid(column=1, row=0, sticky='nesw')

btn3 = Button(win, text='3', height = 5, width = 13, command=lambda: play(1477, 697))
btn3.grid(column=2, row=0, sticky='nesw')

btn4 = Button(win, text='4', height = 5, width = 13, command=lambda: play(1209, 770))
btn4.grid(column=0, row=1, sticky='nesw')

btn5 = Button(win, text='5', height = 5, width = 13, command=lambda: play(1336, 770))
btn5.grid(column=1, row=1, sticky='nesw')

btn6 = Button(win, text='6', height = 5, width = 13, command=lambda: play(1477, 770))
btn6.grid(column=2, row=1, sticky='nesw')

btn7 = Button(win, text='7', height = 5, width = 13, command=lambda: play(1209, 852))
btn7.grid(column=0, row=2, sticky='nesw')

btn8 = Button(win, text='8', height = 5, width = 13, command=lambda: play(1336, 852))
btn8.grid(column=1, row=2, sticky='nesw')

btn9 = Button(win, text='9', height = 5, width = 13, command=lambda: play(1477, 852))
btn9.grid(column=2, row=2, sticky='nesw')

btn_star_sign = Button(win, text='*', height = 5, width = 13, command=lambda: play(1209, 941))
btn_star_sign.grid(column=0, row=3, sticky='nesw')

btn0 = Button(win, text='0', height = 5, width = 13, command=lambda: play(1336, 941))
btn0.grid(column=1, row=3, sticky='nesw')

btn_pound_sign = Button(win, text='#', height = 5, width = 13, command=lambda: play(1477, 941))
btn_pound_sign.grid(column=2, row=3, sticky='nesw')

win.mainloop() 

stream.stop_stream()
stream.close()
p.terminate()

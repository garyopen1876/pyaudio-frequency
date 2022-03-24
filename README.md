# 用python發出聲音

## 聲音三要素

### 音調（頻率）
人耳能聽到20HZ到20000HZ的聲音
![](https://i.imgur.com/EBOmJ50.jpg)

### 響度（振幅）
![](https://i.imgur.com/AwvTZHy.jpg)

### 音色（波形）
![](https://i.imgur.com/I371hD3.jpg)




## 製造正弦波
想要聲音，首先需要有正弦波，所以來寫一個定義正弦波的function
### 正弦波函數
![](https://i.imgur.com/IGMJWW7.png)

一個 頻率為3Hz 持續10S的正弦波

![](https://i.imgur.com/52Ki47K.png)

### 使用numpy用正弦波函數定義一個正弦波:
```python=
import numpy as np

 
def sine(frequency= 3, time= 10, amplitude= 1, theta= 0):   
    return amplitude * np.sin(2 * np.pi * frequency * time + theta)
```

## 使用pyaudio讀取正弦波:
接下來只要讓pyaudio讀取我們製造的正弦波，就能產生出聲音

但是一個正弦波函數值是要怎麼發出聲音?pyaudio聽得懂嗎?
![](https://i.imgur.com/ckRQwtj.jpg)


### 取樣率(sample rate)
從連續訊號中提取並組成離散訊號的取樣個數

![](https://i.imgur.com/zuTPvJ9.jpg)

透過numpy arange去排列每個採樣點時間，並對正弦波去進行採樣
```python=
def sine(frequency= 3, time= 10, amplitude= 1, theta= 0, sample_rate=44100):   

    arange_time = np.arange(0, time, 1/sample_rate)
    
    return amplitude * np.sin(2 * np.pi * frequency * arange_time + theta)
```

### 讓pyaudio來讀喽!
```python=
import numpy as np
import pyaudio

# 剛剛的正弦波取樣function
def sine(frequency= 3, time= 10, amplitude= 1, theta= 0, sample_rate=44100):   

    arange_time = np.arange(0, time, 1/sample_rate)
    
    return amplitude * np.sin(2 * np.pi * frequency * arange_time + theta)

# pyaudio的讀取方法
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,channels=1, rate=44100, output=True)

data =  sine(frequency= 3, time= 10, amplitude= 1, theta= 0, sample_rate=44100)

stream.write(data.astype(np.float32).tobytes())
stream.stop_stream()
stream.close()
p.terminate()

```

當然聽不到 上面有說人耳只能聽到20HZ到20000HZ的聲音...

## 小實作 電話 - 雙音多頻（Dual-Tone Multi-Frequency, DTMF）
![](https://i.imgur.com/oO4o4ff.png)

雙音多頻-程式碼
```python=
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
    sa=np.divide(ss, 2.0)
    return sa
 

    

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,channels=1, rate=44100, output=True)

data = two_sine(1209, 697) # 1號鍵
stream.write(data.astype(np.float32).tobytes())

stream.stop_stream()
stream.close()
p.terminate()
```
## 掃雷區 - pyaudio 安裝失敗問題

出現:

    ERROR: Command errored out with exit status 
    ...
    error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/

原因:
![](https://i.imgur.com/U6miLR1.png)

解決方法:

到[UCI網站](https://www.lfd.uci.edu/~gohlke/pythonlibs/)下載 pyaudio 套件

## 參考資料

[ncyu8880001: (一) 音調、響度、音色 - 嘉義大學開放式課程](http://opencourse.ncyu.edu.tw/ncyu/mod/resource/view.php?id=2275)

[Sine Waves in the Time Domain](https://datacrayon.com/posts/signal-processing/sp-basics/sine-waves-in-the-time-domain/)

[子風的知識庫](https://zwindr.blogspot.com/2017/03/python-pyaudio.html)

[[資訊小知識] 類比訊號 VS 數位訊號](https://ittoos25.pixnet.net/blog/post/305288699-%5B%E8%B3%87%E8%A8%8A%E5%B0%8F%E7%9F%A5%E8%AD%98%5D-%E9%A1%9E%E6%AF%94%E8%A8%8A%E8%99%9F-vs-%E6%95%B8%E4%BD%8D%E8%A8%8A%E8%99%9F)

[[音響研究室] 192Khz？取樣率是什麼？真的數字越高就越好聽嗎？玩數位流一定要懂的 DAC 選購要點！](https://www.cool3c.com/article/88823)

[音頻採樣率都是44100？為什麼](https://kknews.cc/zh-tw/digital/v5p39xy.html)

import pyaudio
import wave

""" Taking the voice input """

chunk = 1024 
sample_format = pyaudio.paInt16  
channels = 2
fs = 16000  
seconds = 60
filename = "audio\yasasi\data.wav"

p = pyaudio.PyAudio()  

print("-------------------------------------------------------------------------------------------")
print('Recording')

stream = p.open(format=sample_format,
				channels=channels,
				rate=fs,
				frames_per_buffer=chunk,
				input=True)

frames = []  


for i in range(0, int(fs / chunk * seconds)):
	data = stream.read(chunk)
	frames.append(data)


stream.stop_stream()
stream.close()

p.terminate()

print('Finished recording')
print("-------------------------------------------------------------------------------------------")
# Save
wf = wave.open(filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()

import wave

obj = wave.open("chill.wav", "rb")

# print("Number of channels", obj.getnchannels())
# print("sample width", obj.getsampwidth())
# print("frame rate", obj.getframerate())
# print("Number of frames", obj.getnframes())
print("parameters", obj.getparams())


t_audio = obj.getnframes()/obj.getframerate()

print (t_audio)

frames= obj.readframes(-1)
print(type(frames), type(frames[0]))

print(len(frames))

obj.close()

# obj_new= wave.open("chill_new.wav", "wb")

# obj_new.setnchannels(1)
# obj_new.setsampwidth(2)
# obj_new.setframerate(16000.0)
# # obj_new.setnframes()

# obj_new.writeframes(frames)

# obj_new.close()

next_sample= wave.open("sample7.wav", "wb")

next_sample.setnchannels(1)
next_sample.setsampwidth(2)
next_sample.setframerate(16000.0)

next_sample.writeframes(frames)

next_sample.close()





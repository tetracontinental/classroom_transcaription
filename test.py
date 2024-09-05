import whisper
import datetime

print("start:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
model = whisper.load_model("small")
result = model.transcribe("sample1.wav")
print(result["text"])
print("end:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


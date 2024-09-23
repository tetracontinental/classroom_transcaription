import sounddevice as sd
import numpy as np
import wavio
from faster_whisper import WhisperModel

# 録音の設定
SAMPLE_RATE = 16000  # サンプリングレート
DURATION = 30  # 録音時間（秒）
AUDIO_FILE_NAME = "recording.wav"

# マイクから音声を録音する関数
def record_audio(duration, sample_rate, filename):
    print("Recording...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()  # 録音が終わるまで待機
    wavio.write(filename, audio, sample_rate, sampwidth=2)  # WAVファイルに保存
    print("Recording finished.")

# 音声を録音
record_audio(DURATION, SAMPLE_RATE, AUDIO_FILE_NAME)

# Whisperモデルを読み込む
model = WhisperModel("large-v3", device="cpu", compute_type="int8")

# 音声ファイルを文字起こしする
segments, info = model.transcribe(
    AUDIO_FILE_NAME,
    beam_size=7,
    vad_filter=True,
    without_timestamps=True,
)

# 言語と確率を表示
print("Detected language '%s' with probability %f" % (info.language, info.language_probability))
for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))

# 録音した音声ファイルを削除（必要に応じて）
# import os
# os.remove(AUDIO_FILE_NAME)
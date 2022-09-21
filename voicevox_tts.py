import core
# コアの初期化
core.initialize(use_gpu=False, cpu_num_threads=4)

# openjtalk辞書のロード
core.voicevox_load_openjtalk_dict("open_jtalk_dic_utf_8-1.11")

# 音声合成
wavefmt = core.voicevox_tts("これは音声合成のテストです", speaker_id=3)  # 3, 13

# 保存
with open("test.wav", "wb") as f:
    f.write(wavefmt)

core.finalize()

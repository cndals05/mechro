import keyboard
import time

# 설정
recordKey = "f2"  # 녹화 키
playKey = "esc"  # 실행 키

# 변수
recording = False
playing = False
keyRecords = []

# 키 바인딩


def recordBind(_):
    global recording
    global playing
    if not playing:
        if recording:
            recording = False
            print("녹화 끝")
        else:
            recording = True
            print("녹화 시작")


def playBind(_):
    global playing
    global recording
    if not recording:
        if playing:
            playing = False
            print("재생 끝")
        else:
            playing = True
            print("재생 시작")


keyboard.on_press_key(recordKey, recordBind)
keyboard.on_press_key(playKey, playBind)

# 메인


def main():
    print("실행")
    while True:
        if recording:  # 키 녹화 중일 경우
            recorded = keyboard.read_key()
            if not recorded in keyRecords and recorded != recordKey and recorded != playKey:  # 읽힌 키가 아직 안 찍힌 키고 재생키랑 녹화키랑 안 겹치면
                keyRecords.append(recorded)
                print(f"{recorded}키 녹화됨")
        elif playing:  # 재생
            for key in keyRecords:
                keyboard.press(key)
                keyboard.release(key)
                time.sleep(1 / 1000)


if __name__ == "__main__":
    main()

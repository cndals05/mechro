import keyboard
import time


def main():
    print("메크로 프로그램을 실행합니다. esc 키를 누르면 실행됩니다.")
    while True:
        keyboard.wait('esc')  # esc 키를 누를 때까지 대기
        print("메크로 프로그램이 시작되었습니다. 지정된 키가 반복해서 실행됩니다.")
        while True:
            keyboard.press('a')  # 실행될 키
            time.sleep(0.02)  # 키를 놓고 대기하는 시간
            keyboard.release('a')
            if keyboard.is_pressed('esc'):  # esc 키가 눌렸다면 반복 중지
                print("메크로 프로그램이 정지되었습니다.")
                break
            if keyboard.is_pressed('ctrl'):  # ctrl 키가 눌렸다면 반복 중지
                print("메크로 프로그램이 정지되었습니다.")
                break


if __name__ == '__main__':
    main()

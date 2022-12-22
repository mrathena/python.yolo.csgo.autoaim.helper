import time

import cv2
from win32con import HWND_TOPMOST, SWP_NOMOVE, SWP_NOSIZE
from win32gui import FindWindow, SetWindowPos

from toolkit import Detector, Timer

region = (3440 // 5 * 2, 1440 // 3, 3440 // 5, 1440 // 3)
weight = 'weights.csgo.public.group.967082372.F4E232C07565A97341070431B91CA46B-v5-s-640-4500-2-T.CT.engine'
detector = Detector(weight)

title = 'Realtime ScreenGrab Detect'
while True:

    begin = time.perf_counter_ns()
    _, img = detector.detect(region=region, image=True, label=True, confidence=True)
    cv2.putText(img, f'{Timer.cost(time.perf_counter_ns() - begin)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 1)
    cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE)
    cv2.imshow(title, img)
    SetWindowPos(FindWindow(None, title), HWND_TOPMOST, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE)
    t3 = time.time()
    k = cv2.waitKey(1)  # 0:不自动销毁也不会更新, 1:1ms延迟销毁
    if k % 256 == 27:
        cv2.destroyAllWindows()
        exit('ESC ...')

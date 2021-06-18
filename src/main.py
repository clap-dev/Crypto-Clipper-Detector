import psutil
import ctypes
import time

class Detector:
    def __init__(self):
        self.detections = set()
        self.user32 = ctypes.windll.user32

    def start_detection(self):
        while True:
            process_id = ctypes.c_ulong()
            clipboard_owner = self.user32.GetClipboardOwner()

            self.user32.GetWindowThreadProcessId(clipboard_owner, ctypes.byref(process_id))

            if process_id.value != 0:
                if process_id.value not in self.detections:
                    process_name = psutil.Process(process_id.value).name()
                    process_path = (process.exe() for process in psutil.process_iter() if process.name() == process_name)

                    print(next(process_path))

                    self.detections.add(process_id.value)

            time.sleep(0.5)

if __name__ == '__main__':
    detector = Detector()
    detector.start_detection()

import ctypes
import psutil
import time

class Detector:
    def __init__(self):
        self.detected = set()

    def start_detection(self):
        while True:
            try:
                process_id = ctypes.c_ulong()

                ctypes.windll.user32.GetWindowThreadProcessId(
                    ctypes.windll.user32.GetClipboardOwner(),
                    ctypes.byref(
                        process_id
                    )
                )

                if process_id.value and process_id.value not in self.detected:
                    process_name = psutil.Process(process_id.value).name()
                    process_path = list(
                        set(
                            process.exe()
                            for process in psutil.process_iter()
                            if process.name() == process_name
                        )
                    )

                    print(
                        '\n'.join(
                            process_path
                        )
                    )

                    self.detected.add(process_id.value)

            except Exception:
                pass

            time.sleep(0.25)

if __name__ == '__main__':
    detector = Detector()
    detector.start_detection()

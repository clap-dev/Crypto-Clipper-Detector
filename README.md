# Crypto Clipper Detector

Simply put, the 21st century has had a upspring in malware. Along the course, came a simple but effective piece of malware that latches onto the infected users clipboard and replaces any crypto address to the attackers personal address. Crypto addresses are very easy to mistake for another, making victims lose money. Simple, yet effective.

![screen-gif](https://clap.shx.gg/cKm5jx.gif)

## Installation

```bash
pip install -e requirements.txt
```

## Usage

```python
python main.py
```

## How does it work?

It's quite simple. Using ctypes to access the lower-level api's, we are able to use the function `GetClipboardOwner` which according to the [MSDN Docs](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getclipboardowner) `"If the function succeeds, the return value is the handle to the window that owns the clipboard."`. This is quite useful as crypto clippers attack the clipboard.

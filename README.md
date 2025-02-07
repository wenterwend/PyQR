# PyQR
A Python Based QR code generator

## Description
PyQR is a simple Python-based QR code generator that allows you to create QR codes from URLs or any other data. The generated QR codes can be saved as image files.

## Features
- Generate QR codes from any data (e.g., URLs, text)
- Save QR codes as image files
- Customizable QR code size and error correction level

## Requirements
- Python 3.x
- `qrcode` library
- `Pillow` library

## Installation
To install the required libraries, run:
```sh
pip install qrcode[pil]

## Example Usage
python main.py "http://domain.com" "C:\\output.png"
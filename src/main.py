
import qrcode
import argparse

def generate_qr(data, output_path):
    # Create QR Code instance
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction used for the QR Code
        box_size=10,  # controls how many pixels each “box” of the QR code is
        border=4,  # controls how many boxes thick the border should be
    )

    # Add data to the instance
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    img.save(output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a QR code from a URL")
    parser.add_argument("data", help="The data (URL) to encode in the QR code")
    parser.add_argument("output_path", help="The file path to save the QR code image")

    args = parser.parse_args()

    generate_qr(args.data, args.output_path)
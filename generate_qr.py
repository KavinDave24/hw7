import qrcode
import logging

# Sets up logging
logging.basicConfig(filename='qr_code.log', level=logging.INFO)

# URL to be encoded in the QR code.
url = 'https://github.com/KavinDave24'

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill='black', back_color='white')

# Save the image
img_file = 'github_qr_code.png'
img.save(img_file)

# Log the successful creation
logging.info('Successfully created QR code and saved as %s', img_file)

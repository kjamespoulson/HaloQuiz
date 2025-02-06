import os
import time
from PIL import Image

# Function to open and display image
def open_image(keyword):
    script_dir = os.path.abspath(os.path.dirname(__file__))
    image_path = os.path.join(script_dir, "images", f"{keyword.lower()}.jpg")

    if os.path.exists(image_path):
        filename = os.path.basename(image_path)
        # image = Image.open(image_path)
        # image.show()
        with open("pipe.txt", "w") as file:
            file.write(f"{filename}\n")
    else:
        print("Image file not found.")

# Listen for changes in pipe.txt
run = True
while run is True:
    with open("pipe.txt", "r") as file:
        content = file.read().strip()

    if content:
        # print(f"Received: {content}")
        if content in ["Grunt", "Flood", "Hunter", "Jackal", "Elite"]:
            open_image(content)
            file.close()
        else:
            # print("Invalid keyword.")
            run = False


    # Wait for a short duration before checking again
    time.sleep(1)

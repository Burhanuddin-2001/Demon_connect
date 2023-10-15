# main.py
from __future__ import annotations
from utils.constants import BROWSER
from utils.constants import USR_DIR
from utils.constants import CHROME_DRIVER_PATH
from api.whatsapp_api import Demon
from colorama import Fore, Style

def main():
    whatsapp_demon = None
    try:


        # Define colors
        blue = Fore.BLUE
        green = Fore.GREEN
        yellow = Fore.YELLOW
        magenta = Fore.MAGENTA
        reset = Style.RESET_ALL

        # Print the text with colors and emojis
        print(f"{blue}👾 Demon Connect Project 👾{reset}")
        print(f"{yellow}Welcome to the Demon Connect project!{reset}")
        print(f"{green}🚀 We are building something amazing. 🚀{reset}")
        print(f"{magenta}🌟 Join us and be part of the magic! 🌟{reset}")


        # Create an instance of the Demon class
        whatsapp_demon = Demon(BROWSER,USR_DIR,CHROME_DRIVER_PATH)

        # Log in to WhatsApp Web
        whatsapp_demon.login()

        # @whatsapp_demon.event
        # def on_message(chat):
        #     print(f"New message from {chat.name}: {chat.message}")

        # chat = whatsapp_demon.open("Anupam Maurya")
        # chat.send("HI")

        # Send a message
        message = "heyy"
        contact = "Grp"
        whatsapp_demon.send_message(contact,message)
        whatsapp_demon.delete_message(contact,message)

        # Send an image (provide the path to the image file)
        # image_path = r"C:\Users\raman\Downloads\aatman.jpg"
        # contact = "Grp"
        # whatsapp_demon.send_image(contact,image_path)


        # Send a video (provide the path to the video file)
        # video_path = "path/to/your/video.mp4"
        # whatsapp_demon.send_video(contact,video_path)

        # tag all in group
        # group_name = "Grp"
        # whatsapp_demon.tag_all(group_name)


    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        # Close the browser when done
        if whatsapp_demon is not None:
            whatsapp_demon.close()

if __name__ == "__main__":
    main()

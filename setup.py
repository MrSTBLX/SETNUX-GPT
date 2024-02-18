# setup.py

import os

print(f"""\033[0m

┌──────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                      │
│               ███████╗████████╗██╗  ██╗     ██████╗ ██████╗ ████████╗                │
│               ██╔════╝╚══██╔══╝╚██╗██╔╝    ██╔════╝ ██╔══██╗╚══██╔══╝                │
│               ███████╗   ██║    ╚███╔╝     ██║  ███╗██████╔╝   ██║                   │
│               ╚════██║   ██║    ██╔██╗     ██║   ██║██╔═══╝    ██║                   │
│               ███████║   ██║   ██╔╝ ██╗    ╚██████╔╝██║        ██║                   │
│               ╚══════╝   ╚═╝   ╚═╝  ╚═╝     ╚═════╝ ╚═╝        ╚═╝                   │
│                                 ┌── SETNUX GPT ──┐                 by @MrSTBLX       │
└──────────────────────────────────────────────────────────────────────────────────────┘
 SETNUX GPT is a powerful, uncensored AI designed by @MRSTBLX and inspired by WormGPT.


""")


def setup_api_key():
    api_key = input("Please enter your OpenAI API key: ")
    with open("key.txt", "w") as file:
        file.write(api_key)

if __name__ == "__main__":
    if os.path.exists("key.txt"):
        overwrite = input("A key file already exists. Do you want to overwrite it? (y/n): ")
        if overwrite.lower() == "y":
            setup_api_key()
        else:
            print("Setup canceled.")
    else:
        setup_api_key()
    print("API key setup completed.")

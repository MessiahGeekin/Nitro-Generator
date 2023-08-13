import string
import random
import requests

BASE_URL = "https://discordapp.com/api/entitlements/gift-codes/"

def code():
    characters = string.ascii_letters + string.digits
    return "".join(random.choices(characters, k=16))

def proxies():
    proxy_list = []
    with open("proxies.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            proxy_list.append(line.strip())
    return proxy_list


def backend():
    proxy_list = proxies()
    for proxy in proxy_list:
        response = requests.get(url=BASE_URL + code(), proxies={"http": proxy, "https": proxy})
        if response.status_code == 200:
            return BASE_URL + code()
    return None  


def main():
    inp = input("How many nitro codes would you like to generate: ")
    if inp.isdigit() and int(inp) >= 1:
        inp = int(inp)
        found_valid_code = False
        for _ in range(inp):
            valid_code = backend()
            if valid_code:
                found_valid_code = True
                print("Valid code:", valid_code)

        if not found_valid_code:
            print("No valid codes")

if __name__ == "__main__":
    main()

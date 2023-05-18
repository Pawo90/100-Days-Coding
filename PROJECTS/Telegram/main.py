import requests

def send_to_telegram(message):


    apiToken = '5900772249:AAGPGTVRjKYF5NChy8LAl_roEmETF31Ch6c'
    chatID = '6177085502'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)

send_to_telegram("Nice Work ;) Your First telegram has been send")
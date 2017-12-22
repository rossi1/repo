from authy import AuthyFormatException
from authy import AuthyApiException
from authy.api import AuthyApiClient


def main():
    try:
        auth('api_key', 'your email here', 'phone_number', 'area_code')
        request_sms('api_key', 'user_id')
   execpt AuthyApiExecption:
          print('unable to connect')


def auth(key, email, phone, area_code):
    authy_api = AuthyApiClient(key)
    user = authy_api.users.create(email, phone, area_code)
    if user.ok():
        print('user id is {}'.format(user.id))
    else:
        print('error occurred!')


def request_sms(api_key, user_id):
    authy_api = AuthyApiClient(api_key)

    try:
        user = authy_api.users.request_sms(user_id=user_id)
        if user.ok:
            verify_token = authy_api.tokens.verify(user_id, input('enter token here: '), {'force': True})
            if verify_token.ok():
                print('token was verified')
            else:
                print('token verification failed')
        else:
            print('could\nt send code')
    except AuthyFormatException:
        print('An exception took place')


if __name__ == '__main__':
    main()

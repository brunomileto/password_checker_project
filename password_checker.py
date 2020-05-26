import requests
import hashlib


def main():
    with open('input_password.txt') as archive:
        password_list = archive.read().split()
        for password in password_list:
            count = pwned_api_check(password)
            if count:
                print('{} was found {} times... you should probably change your password!'.format({password}, {count}))
            else:
                print('{} was NOT found. Your are good. Carry on!'.format({password}, {count}))
        return 'Done!'


def pwned_api_check(password):
    hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_five_character = hashed_password[:5]
    remaining_character = hashed_password[5:]
    response = request_api_data(first_five_character)
    return get_password_leaks_count(response, remaining_character)


def request_api_data(query_character):
    url = 'https://api.pwnedpasswords.com/range/' + query_character
    response = requests.get(url)

    if response.status_code != 200:
        raise RuntimeError('Error fetching:{}, check the API and try again!'.format(response.status_code))
    else:
        return response


def get_password_leaks_count(list_hashes, my_remaining_hash):
    list_hashes = (line.split(":") for line in list_hashes.text.splitlines())
    for h, count in list_hashes:
        if h == my_remaining_hash:
            return count
    return 0


if __name__ == '__main__':
    main()

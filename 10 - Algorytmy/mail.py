def search(my_email, email_list):
    for email in email_list:
        if email == my_email:
            return True

    return False


def main():
    users_emails = ['aaa@a.pl', 'bbb@b.pl', 'ccc@c.pl']
    wanted_email = 'ddd@b.pl'

    result = search(wanted_email, users_emails)
    print('Email on list: ', result)


if __name__ == '__main__':
    main()

def search_email(my_mail, emails):
    if my_mail in emails:
        return True
    else:
        return False




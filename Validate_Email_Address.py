'''
Email Validation and sort the filtered emails
'''
import re
def mail_check(s):
    if re.match("^[A-Za-z0-9-_]+@[A-za-z0-9]+\.[a-zA-Z]{1,3}$",s):
        return True
    return False
def filter_mail(email):
    return list(filter(mail_check,email))

if __name__ == '__main__':
    email = []
    for i in range(int(input())):
        email.append(input())
    filtered_mails = filter_mail(email)
    filtered_mails.sort()
    print(filtered_mails

import sys


def mail_cleaner(file_in, file_out):
    mails = []
    with open(file_in, 'r', encoding='utf8') as f:
        for line in f:
            if line.count('@') == 1:
                mail = line.strip().lower()
                if mail in mails:
                    pass
                else:
                    mails.append(mail)

    with open(file_out, 'w', encoding='utf-8') as f:
        for mail in mails:
            f.write(mail + '\n')


try:
    file_in = sys.argv[1]
    file_out = sys.argv[2]
    # file_in = r'C:\Users\kurs\PycharmProjects\bootcamp\zjazd_4\emails.txt'
    # file_out = r'C:\Users\kurs\PycharmProjects\bootcamp\zjazd_4\cleaned_emails.txt'
    mail_cleaner(file_in, file_out)
except:
    print('Usage: file_in.txt file_out.txt')

import imaplib
import email
from email.header import decode_header

usr_name = "charanbhavisetti2000@gmail.com"
pass_word = "GooglePassword@456"

imap = imaplib.IMAP4_SSL("imap.gmail.com")
imap.login(usr_name, pass_word)

imap.select("INBOX")

status, messages = imap.search(None, 'BEFORE "01-AUG-2018"')

print(messages)
from password_creator import Password
import argparse

args = argparse.ArgumentParser(usage='python password_generator.py -c CHARSET -l LENGTH')
args.add_argument('-c','--charset',required=True)
args.add_argument('-l','--length',default='8')
options = args.parse_args()

password = Password(options.charset,int(options.length))
password.set_charset()
password.generate_password()
print('Your Random Password is {}'.format(password.get_password()))
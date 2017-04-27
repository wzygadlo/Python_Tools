'''
authentication -- who you are
authorization -- what you are permitted
'''

passwords = {}

### Plain text :-( #####################

def store_password(username, password):
    passwords[username] = password

def check_password(username, password):
    return passwords[username] == password


### Two-way Encryption #################

def store_password(username, password):
    passwords[username] = password.encode('rot-13')

def check_password(username, password):
    return passwords[username].decode('rot-13') == password


### One-way Encryption #################

def store_password(username, password):
    passwords[username] = hash(password)

def check_password(username, password):
    return passwords[username] == hash(password)


### Cryptohash ########################

import md5

def store_password(username, password):
    passwords[username] = md5.new(password).hexdigest()

def check_password(username, password):
    return passwords[username] == md5.new(password).hexdigest()


### Modern Cryptohash ##################

import hashlib

def store_password(username, password):
    passwords[username] = hashlib.sha512(password).hexdigest()

def check_password(username, password):
    return passwords[username] == hashlib.sha512(password).hexdigest()


### Add some salt ######################
# salt is per-user, store it with the hashcode

import random, string

alphabet = string.ascii_letters + string.digits + string.punctuation

def good_password(n=20):
    return ''.join(random.choice(alphabet) for i in range(n))

def slowhash(password, salt, repeats=int(1e5)):
    hashcode = hashlib.sha512(password + salt).hexdigest()
    for i in xrange(repeats):
        hashcode = hashlib.sha512(hashcode).hexdigest()
    return hashcode

def store_password(username, password):
    salt = good_password()
    hashcode = slowhash(password, salt)
    passwords[username] = hashcode, salt

def check_password(username, password):
    hashcode, salt = passwords[username]
    return hashcode == slowhash(password, salt)

### Rainbow Table ######################

rainbow = {}

with open('data/common_passwords.txt') as f:
    for line in f:
        password = line.split(', ')[0]
        hashcode = hashlib.sha512(password).hexdigest()
        rainbow[hashcode] = password

if __name__ == '__main__':
    store_password('admin', 'cisco123')
    print check_password('admin', 'cisco123')
    print check_password('admin', 'cisco124')
    print passwords

    # Test Accounts
    crummy_passwords = '''
    admin root superman password cisco snoopy password1
    Password password. password! !password (password)
    '''.split()
    for i, password in enumerate(crummy_passwords):
        username = 'User{:03d}'.format(i)
        store_password(username, password)

    # Rainbow Attack
    fmt = 'Gotcha! {user}: {password}'
    for username, hashcode in sorted(passwords.items()):
        if hashcode in rainbow:
            print fmt.format(user=username, password=rainbow[hashcode])

import hashlib

def substr(string, sub):
    len_sub = len(sub)
    h_subs = hashlib.sha1(sub.encode('utf-8')).hexdigest()
    for i in range(len(string) - len_sub + 1):
        if h_subs == hashlib.sha1(string[i:i+len_sub].encode('utf-8')).hexdigest():
            return True
    return False

print(substr('i want you to stay', 'ou'))
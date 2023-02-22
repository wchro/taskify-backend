import bcrypt

def gen_hash(password: bytes):
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed

def check_pswd(password: bytes, hashed: bytes):
    return bcrypt.checkpw(password, hashed)



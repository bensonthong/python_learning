filename = 'alice.txt'
# encoding argument is used when system's default encoding doesn't match the encoding of file that's being read.
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"{filename} does not exist")

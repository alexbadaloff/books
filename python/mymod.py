def countLines(name):
    f = open(name)
    ln = f.readlines()
    print('lines',len(ln))
    f.close()

def countChars(name):
    f = open(name)
    ln = f.read()
    print('chars',len(ln))
    f.close()

def test(name):
    countLines(name)
    countChars(name)

if __name__ == "__main__":
    countLines("mymod.py")
    countChars("mymod.py")
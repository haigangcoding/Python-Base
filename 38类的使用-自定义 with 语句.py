class Testwith():
    def __enter__(self):
        print('run')
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print('��������')
        else:
            print('has error %s' %exc_tb)

with Testwith():
    print('Test is running')
    raise NameError('testNameError')
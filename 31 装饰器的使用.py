def tips(func):
    def nei(a, b):
        print('start')
        func(a, b)
        stop('stop')
    return nei()

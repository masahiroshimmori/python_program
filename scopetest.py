
def main():
    test = 'test1'
    test2 = scopetest(test)
    print(test2)


def scopetest(test):
    print(test)
    test = "test2"
    print(test)
    return test

if __name__ == '__main__':
    main()
from testclass.test_test_class import test

def main():
    testclass = test()
    testclass.set_test(10)
    rtn_list = testclass.get_test()

    for rtn in rtn_list:
        print(rtn)

if __name__ == "__main__":
    main()
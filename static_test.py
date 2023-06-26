from testclass import static_class

def main():
    # インスタンスを2つ生成
    my1 = static_class.Error_info()
    rtn = my1.rtn_counter() # 2
    print(rtn)
    my2 = static_class.Error_info()
    rtn = my2.rtn_counter() # 2
    print(rtn)

if __name__ == "__main__":
    main()
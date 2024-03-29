# パイソンではリストや辞書型を関数の引数として渡した場合、実態が渡される（参照型）
def change(l_dict):

    if l_dict['name'] is None:
        l_dict['name'] = "tanaka"

def main():
    stack_list = []
    l_records = [{'order_no' : 'R001', 'name' : 'yamada'}, 
        {'order_no' : 'R002', 'name' : None}, {'order_no' : 'R003', 'name' : 'suzuki'}, {'order_no' : 'R004', 'name' : None}]

    for l_record in l_records:
        l_dict = dict()
        l_dict['order_no'] = l_record['order_no']
        l_dict['name'] = l_record['name']

        change(l_dict)

        stack_list.append(l_dict)
    print(stack_list)

if __name__ == '__main__':
    main()
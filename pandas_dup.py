import pandas as pd
# 登録したいデータ(9パターン)
register_list = [{'order_no':'R001', 'estimate':'R001-001','work_ym':'202112', 'user':'shimmori', 'update':'2022-01-11'},{'order_no':'R001', 'estimate':'R001-002','work_ym':'202112', 'user':'shimmori', 'update':'2022-01-12'},{'order_no':'R001', 'estimate':'R001-003','work_ym':'202112', 'user':'shimmori', 'update':'2022-01-13'},{'order_no':'R002', 'estimate':'R002-001','work_ym':'202112', 'user':'shimmori', 'update':'2022-01-14'},{'order_no':'R002', 'estimate':'R002-002','work_ym':'202112', 'user':'shimmori', 'update':'2022-01-15'},{'order_no':'R002', 'estimate':'R002-003','work_ym':'202112', 'user':'shimmori', 'update':'2022-01-16'},{'order_no':'R003', 'estimate':'R003-001','work_ym':'202112', 'user':'shimmori', 'update':'2022-01-17'},{'order_no':'R003', 'estimate':'R003-002','work_ym':'202112', 'user':'shimmori', 'update':'2022-01-18'},{'order_no':'R003', 'estimate':'R003-003','work_ym':'202112', 'user':'shimmori', 'update':'2022-01-19'}]
# すでに持っているデータ(6パターン)
comp_list = [{'order_no':'R001', 'estimate':'R001-001','work_ym':'202112'},{'order_no':'R001', 'estimate':'R001-003','work_ym':'202112'},{'order_no':'R002', 'estimate':'R002-001','work_ym':'202112'},{'order_no':'R002', 'estimate':'R002-002','work_ym':'202112'},{'order_no':'R003', 'estimate':'R003-002','work_ym':'202112'},{'order_no':'R003', 'estimate':'R003-003','work_ym':'202112'}]
# 期待値としてはoder_no=R001 estimate=R001-002 work_ym=202112  と  oder_no=R002 estimate=R002-003 work_ym=202112  と  oder_no=R003 estimate=R003-001 work_ym=202112  がピックアップされること
df1 = pd.DataFrame(register_list)
df2 = pd.DataFrame(comp_list) #ここは変換する必要ないかもしれない
df3 = pd.concat([df1,df2]).drop_duplicates(subset=['order_no','estimate','work_ym'], keep=False)
dict_df3 = df3.to_dict('records')
print(df1,'\n\n',df2,'\n\n',dict_df3)
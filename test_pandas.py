from asyncio.windows_events import NULL
import pandas as pd

def main():

    l_id = pd.read_csv('csv/id.csv')

    none_pd = l_id.where(l_id.notnull(), None)

    print(none_pd)
    #none_pd_records = none_pd.to_dict('records')
   #for none_pd_record in none_pd_records:
    #    if isinstance(none_pd_record["pre"], (int,float)):
     #       none_pd_record["order_no"] = 0
     #       print(none_pd_record["order_no"])
if __name__ == "__main__":
    main()
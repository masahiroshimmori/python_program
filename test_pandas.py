from asyncio.windows_events import NULL
import pandas as pd

def main():

    l_id = pd.read_csv('csv/id.csv')
    l_id.fillna({'city':0}, inplace=True)
    print(l_id)

if __name__ == "__main__":
    main()
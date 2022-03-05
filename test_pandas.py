import pandas as pd

def main():

    l_id = pd.read_csv('csv/id.csv')

    none_pd = l_id.where(l_id.notnull(), None)

    print(none_pd)

if __name__ == "__main__":
    main()
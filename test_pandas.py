from asyncio.windows_events import NULL
import pandas as pd

def main():

    l_id = pd.read_csv('csv/id.csv')
<<<<<<< HEAD
    l_id.fillna({'city':0}, inplace=True)
    print(l_id)
=======

    none_pd = l_id.where(l_id.notnull(), None)

    print(none_pd)
>>>>>>> 4d1693c3f9365fd2d47b5f2c64947ec5dbda2751

if __name__ == "__main__":
    main()
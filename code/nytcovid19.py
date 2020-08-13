#! python3

import os
import requests
import zipfile 

def download():


    covid_zip = 'https://github.com/nytimes/covid-19-data/archive/master.zip'

    #file_object = requests.get(covid, stream=True)
    file_object = requests.get(covid_zip)

    open('covid.zip', 'wb').write(file_object.content)

    loc = r"C:\Users\AlanB\Documents\Learning - Data\99 Projects\Covid-19"

    with zipfile.ZipFile('covid.zip', 'r') as zip_ref:
        zip_ref.extractall(loc)

    os.remove('covid.zip')

if __name__=='__main__':
    download()

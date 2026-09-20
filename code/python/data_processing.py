import os,csv
file_path=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
#script to open a csv file
try:
    with open(os.path.join(file_path,'Data','Data_collected_with_google_form.csv'),mode='rt') as fic:
        print("The file is open")
except Exception as exc:
    print("The file could not be opened:", os.strerror(exc.errno))

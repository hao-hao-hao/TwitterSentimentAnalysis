import csv


class Csv_helper:
    @staticmethod
    def write_to_file(objs,filename):
        with open(filename+'.csv', 'w') as csvfile:
            fieldnames = list(objs[0].__dict__.keys())
            writer = csv.DictWriter(csvfile,lineterminator='\n', fieldnames=fieldnames)
            writer.writeheader()
            for obj in objs:
                try:
                    writer.writerow(obj.__dict__)
                except:
                    print("Writting Error:" + obj.text)
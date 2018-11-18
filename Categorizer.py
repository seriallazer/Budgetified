import csv
import config_file

class Categorizer:
    def __init__(self):
        self.catfile = open(config_file.category_file, 'r')
        self.cat_reader = csv.reader(self.catfile, delimiter=';')
        self.cat_mapping = {row[0]: row[1] for row in self.cat_reader}
        self.uncatfile_w = open(config_file.uncategorized_file, 'a')
        self.uncat_writer = csv.writer(self.uncatfile_w, delimiter=';')

        self.uncatfile_r = open(config_file.uncategorized_file, 'r')
        self.uncat_reader = csv.reader(self.uncatfile_r, delimiter=';')
        self.uncat_list = []
        for row in self.uncat_reader:
            self.uncat_list.append(row[0])

    def get_category_mapping(self, desc, val):
        return_list = [value for key, value in self.cat_mapping.items() if key in desc]
        category = config_file.get_default_category(val)
        if len(return_list) > 0:
            category = return_list[0]
            return category

        # Try to get top two suggestions for new transactions
        business_name = (desc.split())[0]
        suggestion_list = set([value for key, value in self.cat_mapping.items() if business_name in key][0:2])

        if desc not in self.uncat_list:
            if len(suggestion_list) > 0 :
                self.uncat_writer.writerow([desc, category, suggestion_list])
            else:
                self.uncat_writer.writerow([desc, category])
            self.uncat_list.append(desc)
        return category

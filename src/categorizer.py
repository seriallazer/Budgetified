import csv
import config_file
import os

class Categorizer:
    def __init__(self, recategorize = True, logger = None):
        if logger is None:
            logfile = os.getcwd() + "/categorizer.logs"
            self.logger = open(logfile, 'w')
        else:
            self.logger = logger
        if recategorize:
            self.reapply_category_rules()
            self.prune_uncat_file = True

        self.catfile = open(config_file.category_file, 'r')
        self.cat_reader = csv.reader(self.catfile, delimiter=';')
        self.cat_mapping = {row[0]: row[1] for row in self.cat_reader}

        self.uncatfile_r = open(config_file.uncategorized_file, 'r')
        self.uncat_reader = csv.reader(self.uncatfile_r, delimiter=';')
        self.uncat_list = []

        for row in self.uncat_reader:
            self.uncat_list.append(row[0])

        self.uncatfile_w = open(config_file.uncategorized_file, 'a')
        self.uncat_writer = csv.writer(self.uncatfile_w, delimiter=';')

    def reapply_category_rules(self):
        uncat_items = []
        cat_items = []
        ucr = open(config_file.uncategorized_file, 'r')
        csv_ucr = csv.reader(ucr, delimiter=';')
        for row in csv_ucr:
            if len(row) == 2 and config_file.is_default_category(row[1]) is False:
                cat_items.append(row)
                self.logger.write(
                    '[Categorizer] Following item moved from Uncategorized to Categorized: %s \n' % (str(cat_items[-1])))
            elif len(row) == 4 and row[3] == config_file.approved_sign:
                sugg_list = row[2].strip('{').strip('}').split(',')
                sugg_cat = sugg_list[0].strip('\'')
                cat_items.append([row[0], sugg_cat])
                self.logger.write(
                    '[Categorizer] Following item moved from Uncategorized to Categorized: %s \n' % (str(cat_items[-1])))
            else:
                uncat_items.append(row)
        ucr.close()

        cw = open(config_file.category_file, 'a')
        csv_cw = csv.writer(cw, delimiter=';')
        for row in cat_items:
            self.logger.write('[Categorizer] Appending to Categorized-list %s \n' % (str(row)))
            csv_cw.writerow(row)
        cw.close()

        ucw = open(config_file.uncategorized_file, 'w')
        csv_ucw = csv.writer(ucw, delimiter=';')
        for row in uncat_items:
            self.logger.write('[Categorizer] Writing to Uncategorized-list %s \n' % (str(row)))
            csv_ucw.writerow(row)
        ucw.close()

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

from tika import parser as tikaparser
import config_file, categorizer
import os
import hashlib

class Parser:
    def __init__(self, logger = None):
        self.categorizer = categorizer.Categorizer();
        if logger is None:
            logfile = os.getcwd() + "/parser.logs"
            self.logger = open(logfile, 'w')
        else:
            self.logger = logger

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def get_pdf_content(self, path):
        raw = tikaparser.from_file(path)
        pdf_text = raw['content']
        self.logger.write("[Parser] Pdf-data extracted for: " + path)
        return pdf_text

    def parse_identifier(self, type, line):
        if type == 'DBS_CREDIT' and 'NEW TRANSACTIONS' in line:
            return True
        if type == 'DBS_ACCOUNT' and 'CURRENCY SINGAPORE DOLLAR' in line:
            return True
        return False

    def create_transaction_hashid(self, transaction):
        transaction_str = str(transaction)
        hash_object = hashlib.md5(transaction_str.encode())
        return hash_object.hexdigest()

    def parse_statement(self, path, origin):
        pdf_text = self.get_pdf_content(path)
        start_parsing = False
        year = "2018"
        stmt_transactions = []

        for line in pdf_text.splitlines():
            tokens = line.strip().split()
            token_size = len(tokens)
            if token_size <= 3:
                continue

            # print("try ||",start_parsing,"||",tokens[0],"||",tokens[1],"||",self.is_number(tokens[-1]))
            if type == 'DBS_CREDIT' and start_parsing and (tokens[1] in config_file.Months) and tokens[
                0].isnumeric() and (self.is_number(tokens[-1]) or tokens[-1] == 'CR') and token_size > 3:
                date = int(year + config_file.Months[tokens[1]] + tokens[0].zfill(2))
                val_col = -1
                transaction_val = float(tokens[-1])
                if tokens[-1] == 'CR':
                    val_col = -2
                    transaction_val = -1 * float(tokens[-2])
                desc = ' '.join(tokens[2:val_col])
                balance = 'NA'
                category = self.categorizer.get_category_mapping(desc, -1 * transaction_val)
                transaction_details = [date, desc, transaction_val, origin, category, balance]
                hashid = self.create_transaction_hash(transaction_details)
                #assert isinstance(hashid, object)
                transaction_details.append(hashid)
                expense = dict(zip(config_file.transaction_template, transaction_details))
                stmt_transactions.append(expense)

            if not start_parsing:
                start_parsing = self.parse_identifier(type, line)

        return stmt_transactions
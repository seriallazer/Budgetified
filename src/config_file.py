import hashlib
import sys

print(sys.version)

Months = dict(JAN='01', FEB='02', MAR='03', APR='04', MAY='05', JUN='06', JUL='07', AUG='08', SEP='09', OCT='10',
              NOV='11', DEC='12')
old_category_file = '/Users/mayankgupta/Documents/Budget/Categories_all.csv'
category_file = '/Users/mayankgupta/Documents/Budgetified/Categories_all_NEW.csv'
uncategorized_file = '/Users/mayankgupta/Documents/Budgetified/Uncategorized_Transactions.csv'
default_accounts_dir = '/Users/mayankgupta/Documents/Budgetified/Accounts/'
archive_subdir = '/archive_files/'
default_income_category = 'Income|Misc'
default_expense_category = 'Expenses|Misc'

transaction_template = ['date', 'desc', 'tval', 'origin', 'category', 'balance', 'hashid']
writer_format = '%d ; %-100s ; %10s ; %30s ; %50s ; %10s ; %30s \n'
approved_sign = 'A'

def is_default_category(category_desc):
    return (category_desc == default_expense_category) | (category_desc == default_income_category)

def get_default_category(val):
    if float(val) > 0:
        return default_income_category
    return default_expense_category


def create_transaction_hash(transaction_detail_list):
    return hashlib.md5(str(transaction_detail_list).encode()).hexdigest()


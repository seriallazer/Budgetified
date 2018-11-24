import hashlib

Months = dict(JAN='01', FEB='02', MAR='03', APR='04', MAY='05', JUN='06', JUL='07', AUG='08', SEP='09', OCT='10',
              NOV='11', DEC='12')
old_category_file = '/Users/mayankgupta/Documents/Budget/Categories_all.csv'
category_file = '/Users/mayankgupta/Documents/Budgetified/Categories_all_NEW.csv'
uncategorized_file = '/Users/mayankgupta/Documents/Budgetified/Uncategorized_Transactions.csv'
default_accounts_dir = 'Users/mayankgupta/Documents/Budgetified/Accounts/'
archive_subdir = '/archive_files/'
default_income_category = 'Income|Misc'
default_expense_category = 'Expenses|Misc'

transaction_template = ['date', 'desc', 'tval', 'origin', 'category', 'balance', 'hashid']


def get_default_category(val):
    if val > 0:
        return default_income_category
    return default_expense_category


def create_transaction_hash(transaction_detail_list):
    return hashlib.md5(str(transaction_detail_list).encode()).hexdigest()


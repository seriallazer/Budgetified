
Months = dict(JAN='01', FEB='02', MAR='03', APR='04', MAY='05', JUN='06', JUL='07', AUG='08', SEP='09', OCT='10',
              NOV='11', DEC='12')
old_category_file = '/Users/mayankgupta/Documents/Budget/Categories_all.csv'
category_file = '/Users/mayankgupta/Documents/Budget/Categories_all_NEW.csv'
uncategorized_file = '/Users/mayankgupta/Documents/Budgetified/Uncategorized_Transactions'
default_income_category = 'Income|Misc'
default_expense_category = 'Expenses|Misc'

def get_default_category(val):
    if val > 0:
        return default_income_category
    return default_expense_category
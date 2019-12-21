# Budgetified
Smart Personal Finance Categorizer

Budgetified helps you with interesting insights on your Income, Expenses and even Investments. It directly digests e-statements (DBS credit-card statements for now) with least manual intervention involved.
Unlike other similar apps in the category, you no longer have to manually enter details for each expense-item individually. This makes it super-easy to use.

The Categorizer engine is two fold:
1. Prioritizes the expense-information from your own past-evpense categories, ELSE
2. Uses the Smart-Categorizer based on Google-search results on the expense-description
(To enable the Smart-Categorizer you'll need Google-Developer api-key, as of Dec, 2019 its free for upto 150 requests/day)

How to use:
1. Setup an Account folder and download all your e-statements into the folder
2. Add appropriate config-parameters in the config_file.py file
3. Run aggregator.py with arg --parse_all_statements (you may explore other args too)

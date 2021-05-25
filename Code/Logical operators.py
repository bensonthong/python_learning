# Multiple conditions
# if applicant has high income AND good credit
#   Eligible for loan

has_high_income = False
has_good_credit = True
if has_high_income or has_good_credit:
    print("Eligible for loan")

# if has_high_income and has_good_credit:
#     print("Eligible for loan")

# AND: both
# OR: at least one
# NOT: opposite

# if applicant has good credit and doesn't have a criminal record
# then eligible for loan

has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
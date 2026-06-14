import git_functions
from git_functions import *

# 选github之后传到这
def github_menu():
    print("************ github menu ************")
    print("1. <Search Specific Projects>")
    print("2. <Search Users>")
    print("3. <Search Hot Projects>")
    print("4. Can't decide? Tap to check details")
    print("*************************************")
    choose = int(input("please input your choose"))
    if choose == 1:
        get_repos_info()
    elif choose == 2:
        get_user_info()
    elif choose == 3:
        print("33333")
    elif choose == 4:
        print("44444")
    else:
        print("please input a valid choice")




# main
print("***** 1.github    *****")
print("***** 2.wikipedia *****")
platform = input("please choose your platform 1 or 2:")
if (platform == "1"):
    github_menu()
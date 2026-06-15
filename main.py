import git_functions
import print_functions
from git_functions import *

# 选github之后传到这
def github_menu():
    print("************ github menu ************")
    print("1. <Search Specific Projects>")
    print("2. <Search Users>")
    print("3. <Search Hot Projects>")
    print("4. <Search Project By Keyword>")
    print("5. Can't decide? Tap to check details")
    print("*************************************")
    choose = int(input("please input your choose"))
    if choose == 1:
        get_repos_info()
    elif choose == 2:
        get_user_info()
    elif choose == 3:
        get_hot_projects()
    elif choose == 4:
        search_projects_by_keyword()
    elif choose == 5:
        print("Please tap to check details")
    else:
        print("please input a valid choice")




# main
github_menu()
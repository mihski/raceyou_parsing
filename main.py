from http import cookies
from func import autorization, find_names_Piter,CounterPages,count_reqests_page_in_litera

#if __name__=="__main__":

autorization()
cookies,driver= autorization()
#count_reqests_page_in_litera(cookies)    
CounterPages(driver)    
find_names_Piter(driver)

    #input(("Нажми Enter, когда закончишь..."))
    


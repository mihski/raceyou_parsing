from func import autorization, find_names_Piter,CounterPages




if __name__=="__main__":

    driver =autorization()
    CounterPages(driver)
    #find_names_Piter(driver)

    #input(("Нажми Enter, когда закончишь..."))
    driver.quit()


#This function is used to track clicks for 'next page' and 'previous page' button and return 5 pages per entry
def page(counter, custom_data_list):
    dict = {0:0, 1:25, 2:50, 3:75}
    return custom_data_list[dict[counter]:dict[counter]+25]



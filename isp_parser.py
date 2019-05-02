#Parsing the HTML
from bs4 import BeautifulSoup as bs


def tag_to_string(tag_item): # converts bs4.element.tag datatype to string datatype
  string = tag_item.get_text()
  
  return string

def page_parser(response): # parses the html response; passes data to formatter function for formatting
    soup = bs(response.content, features="html.parser")


    table_datas = soup.select('td')
    return formatter(table_datas)


def formatter(table_data):

    data_list = list(map(tag_to_string, table_data)) # maps each list item to tag_to_string function; 
                                                     # converts the returned data to list

    counter = 0
    while "" in data_list and counter<6: #removes empty "" from data_list 
      data_list.remove("")
      counter +=1

    non_empty_data_list = list(map(str.strip, data_list))
    non_empty_data_list.append("") 

    data_dict = {}
    for i in range(0, len(non_empty_data_list), 2):
      data_dict[non_empty_data_list[i]] = non_empty_data_list[i+1]

    return data_dict
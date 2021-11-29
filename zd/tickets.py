import requests
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from authentication import url, user, token, authenticate_user


# Importing json File from Zendesk API to read ticket information
dictionary = authenticate_user(url, user, token)

# Function to call dictionary
#Error Handling
if dictionary == 'error_api_not_available':
    custom_data_list = ()
    error_message = 'Error, API is not available, Please try again later!'
    additional_information = {"Error":"Error, API is not available"}

else:
    # Since there was no error, we can clear our error message
    error_message = ''

    # If import is successful, creating lists to sort different data for initial display on home-page
    ticket_id_list  = []
    ticket_subject_list = []
    ticket_created_list = []
    ticket_status_list = []

    # Sorting tickets information from json information pulled from zendesk API
    ticket_information = dictionary['tickets']

    # Appending all information to the lists we made above
    for items in ticket_information:
        ticket_id_list.append(items['id'])
        ticket_subject_list.append(items['subject'])
        ticket_created_list.append(items['created_at'])
        ticket_status_list.append(items['status'])

    # Merging the custom data into a separate list of tuples to send to index page static website
    # This function creates a tuple of tuples (front page display data) to push in a HTML Table for static website

    custom_data_list = []
    for items in range(len(ticket_information)):
        custom_data_list.append((ticket_id_list[items], ticket_subject_list[items],
                        ticket_created_list[items][0:10], ticket_status_list[items] ,ticket_id_list[items]))

    custom_data_list = tuple(custom_data_list)

    # This function creates a dictionary of a list
    # We map tickets data (presented as a list from Zendesk API) to a dictionary for easy display of additional ticket information display (This is for view more data)
    def list_to_dictionary(List):
        dictionary = {i+1: List[i] for i in range(0, len(List))}
        return dictionary

    additional_information = list_to_dictionary(ticket_information)

    # we use this function to map 'view' button for additional display to actual ticket information in zendesk API
    def map_dictionary(ticket_id, dictionary):
        return dictionary[ticket_id]
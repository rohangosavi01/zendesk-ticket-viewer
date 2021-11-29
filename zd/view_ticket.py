def view_ticket_info(dictionary, number):
    
    ticket_information = dictionary[number]
    ticket_subject = ticket_information['subject']
    ticket_created = (ticket_information['created_at'][0:10] + ' , ' + ticket_information['created_at'][11:19])
    ticket_status = ticket_information['status']
    ticket_description = ticket_information['description']
    ticket_requester = ticket_information['requester_id']
    ticket_priority = ticket_information['priority']
    custom_dictionary = {'Ticket Priority':ticket_priority, 'Subject': ticket_subject, 'Description':ticket_description, 'Status':ticket_status, 'Requester ID':ticket_requester, 'Created On':ticket_created}
    return custom_dictionary

    



    

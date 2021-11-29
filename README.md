# Zendesk Coding Challenge 2021

## About

Welcome to my Ticket Viewer Program !
This is a static web-application, that displays tickets for a company connecting to Zendesk API and showing more details if requested. This static web-application is made using python programming language and flask web-framework. 

## Installations

- [Python](https://www.python.org/downloads/) v3.8.0 or greater
- [Flask](https://flask.palletsprojects.com/en/2.0.x/installation/#install-flask) (Python Version 3.7 or greater)

## Running on your local machine

1. Download this repository to your local machine. 

```
$ git clone https://github.com/rohangosavi01/zendesk-ticket-viewer
```

2. Open this folder in your terminal/cmd prompt and run the following code:
```
$ python app.py
```
or 
```
$ Flask run
```
3. You should see a localhost server running, copy this address into any browser to begin.

## Set-up 

1. The Landing Page consists a Table that displays basic iformation of ticket. 
2. The 'view' button directs to the ticket specific information with more fields. 
3. There are 'Previous Page' and 'Next Page' buttons that help you navigate through 25 pages per item. 
4. More details can be added as needed with requests made to the python dictionary. 
5. Error Handeling =>
   - Invalid API Call => The program displays an error message if there is a problem with API Call, or the response is not as expected. 
   - 404 Page Not Found => If the user is directed to a page which is not in the server, a 404-Error Page is added to help user navigate back to homepage.

## Descriptions 

- ```app.py``` : Program entry point
- ```authentication.py``` : Makes requests to the Zendesk API and returns tickets in Python Dictionary Format
- ```page_tracker.py``` : This tracks the current website page and returns next/previous page having 25 tickets
- ```tickets.py and view_ticket.py``` : Parse Json File data to display texts both in list and indiviual views

## Refrences and Learning Outcomes

- Learning Outcomes 
    - Learned more about API requests, how to parse JSON data and manipulate it.
    - Learned more about HTML, CSS use with Jinja2 tools to parse variables to display dynammic data. 
    - Learned more about Python Web Application enviornment, HTTP Requests and authentication.

- Zendesk API Documentation    
    - https://developer.zendesk.com/api-reference/
    - https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/

- Python & Flask 
    - https://flask.palletsprojects.com/en/2.0.x/tutorial/index.html
    - https://www.youtube.com/watch?v=Z1RJmh_OqeA&t=1917s

## Photos: 

<img width="1840" alt="Screen Shot 2021-11-29 at 04 43 17 1" src="https://user-images.githubusercontent.com/64428362/143854180-0e8b8388-159b-4fb7-a26e-a7b64244b856.png">

<img width="1840" alt="Screen Shot 2021-11-29 at 04 43 26" src="https://user-images.githubusercontent.com/64428362/143854221-810c6919-0b82-4882-9c42-950804c65cf4.png">

<img width="1840" alt="Screen Shot 2021-11-29 at 04 43 45" src="https://user-images.githubusercontent.com/64428362/143854262-a3855af8-f467-4adb-bff2-129ab5a482e0.png">

<img width="976" alt="Screen Shot 2021-11-29 at 04 44 01" src="https://user-images.githubusercontent.com/64428362/143854289-49b00b6a-a863-4889-854d-75700e4ae056.png">






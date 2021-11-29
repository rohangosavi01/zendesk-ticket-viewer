# Zendesk Coding Challenge 2021 

This static web application is made using python programming language and flask web framework

## Prerequisite Installations

- [Python3.8.8](https://www.python.org/downloads/) v3.8.8 or greater
- Flask framwork

## Running this on your server (MacOS/Windows)

1. Download the repository to your local machine with the following code.

```
$ git clone https://github.com/rohangosavi01/zendesk-ticket-viewer
```

2. Open the folder ZD on your terminal and run the following code:
```
$ python app.py 

```
or 

```
$ Flask run

```

### File Description and Error Handling

- ```app.py``` : Program entry point
- ```authentication.py``` : Makes requests to the Zendesk API and returns tickets in Python Dictionary Format
- ```index.html``` : Static webpage to show all tickets
- ```tickets.py and view_ticket.py``` : Parse Json File data to meaningful content online

- If the API is not called correctly, a text is displayed to users. 
- Error Page 404 is added and link back to home so users can return to main menu. 

### About Me 

I am Rohan Gosavi, sophmore at Texas Tech and have experience in python programming language, flask web framework as I have experince in it. I struggled in the pagination process, but was able to complete everything else described the project.

### Refrences and Learning Outcomes

- Learning Outcomes 
    - Learned more about API Handeling and implementing them online. 

- Zendesk API Documentation    
    - https://developer.zendesk.com/api-reference/
    - https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/

- Python & Flask 
    - https://flask.palletsprojects.com/en/2.0.x/tutorial/index.html

- Relevant Courework ENGR1330, CS1382, and Principles of programming


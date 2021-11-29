from flask import Flask, render_template, request, session
from tickets import custom_data_list, additional_information, error_message
from page_tracker import page
from view_ticket import view_ticket_info


# This is our program entry point! 
app = Flask(__name__)
app.secret_key = 'ZendeskCodingChallenge'
global counter
counter = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', data = custom_data_list[0:25], error_message = error_message)
 
@app.route('/ticket', methods=['GET', 'POST'])
def ticket():
    ticket_details = request.form.get('action')
    ticket_details_dictionary = view_ticket_info(additional_information, int(ticket_details))
    return render_template('ticket.html', results = ticket_details_dictionary, ticket_id = ticket_details)

@app.route('/tracker', methods=['GET', 'POST'])
def tracker():
    if request.method == 'POST':
        if request.form.get("previous"):
            global counter
            counter -= 1
            if counter < 1: 
                counter = 0 
            elif counter > 3 or counter == 3: 
                counter = 3           
            return render_template('index.html', data=page(counter, custom_data_list), error_message=error_message)
    
        elif request.form.get("next"):
            counter += 1
            if counter > 3 or counter == 3:
                counter = 3           
            elif counter < 1: 
                counter = 1          
            return render_template('index.html', data=page(counter, custom_data_list), error_message=error_message)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('four_o_four.html'), 404

if __name__ == "__main__":
    app.run(debug = True)


     

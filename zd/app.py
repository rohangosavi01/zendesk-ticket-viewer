from flask import Flask, render_template, request
from tickets import custom_data_list, additional_information, error_message
from view_ticket import view_ticket_info

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', data = custom_data_list, error_message = error_message)

 
@app.route('/ticket', methods=['GET', 'POST'])
def ticket():
    ticket_details = request.form.get('action')
    ticket_details_dictionary = view_ticket_info(additional_information, int(ticket_details))
    return render_template('ticket.html', results = ticket_details_dictionary, ticket_id = ticket_details)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('four_o_four.html'), 404

if __name__ == "__main__":
    app.run(debug = True)


     

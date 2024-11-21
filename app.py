from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# List to hold builder data (as an example)
builders = [
    {"name": "Builder 1", "status": "Available", "upgrade_time": "1 hour", "cost": "1000 Gold"},
    {"name": "Builder 2", "status": "Busy", "upgrade_time": "2 hours", "cost": "2000 Gold"},
    {"name": "Builder 3", "status": "Available", "upgrade_time": "30 minutes", "cost": "500 Gold"}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/builder-status')
def builder_status():
    return render_template('builder_status.html', builders=builders)

@app.route('/add-builder', methods=['GET', 'POST'])
def add_builder():
    if request.method == 'POST':
        # Get data from the form
        builder_name = request.form['builder_name']
        builder_status = request.form['builder_status']
        upgrade_time = request.form['upgrade_time']
        cost = request.form['cost']
        
        # Add new builder to the list
        new_builder = {
            "name": builder_name,
            "status": builder_status,
            "upgrade_time": upgrade_time,
            "cost": cost
        }
        builders.append(new_builder)
        
        # Redirect back to builder status page
        return redirect(url_for('builder_status'))

    return render_template('add_builder.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)


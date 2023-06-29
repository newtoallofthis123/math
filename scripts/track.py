import os
import json
from flask import Flask, render_template, request, jsonify
from fire import Fire
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def init():
    os.chdir(os.path.join(BASE_DIR, 'tracker'))

def get_days():
    with open('info.json') as f:
        data = json.load(f)
    return data['days']

def add_day():
    with open('info.json') as f:
        data = json.load(f)
    data['days'] += 1
    with open('info.json', 'w') as f:
        json.dump(data, f)
    
def write_tracker(info):
    with open('days/day-{}.md'.format(get_days()), 'w') as f:
        f.write(info)

def write_info(info):
    init()
    title = info['title']
    overall = info['overall']
    covered = info['covered']
    pending = info['pending']
    comments = info['comments']
    with open('days/day-{}.md'.format(get_days()), 'w') as f:
        f.write('# Day {}\n\n'.format(get_days()))
        f.write('## {}\n\n'.format(title))
        f.write('This is day {} of my math tracker\n'.format(get_days()))
        f.write("Today is {}\n\n".format(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
        f.write('### Overall\n\n')
        f.write("Overall summary of the day's work:\n\n")
        f.write('{}\n\n'.format(overall))
        f.write('### Covered\n\n')
        f.write("Any work that was covered during the day:\n\n")
        f.write('{}\n\n'.format(covered))
        f.write('### Pending\n\n')
        f.write("Any pending work that will be carried over to the next day:\n\n")
        f.write('{}\n\n'.format(pending))
        f.write('### Comments\n\n')
        f.write("Any comments or observations:\n\n")
        f.write('{}\n'.format(comments))
        f.write('> Written by NoobScience on {}\n'.format(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
        add_day()

def md():
    app = Flask(__name__)
    @app.route('/')
    def index():
        return render_template('index.html')
    @app.route('/submit', methods=['POST'])
    def submit():
        if request.method == 'POST':
            form = request.form
            write_info(form)
            return jsonify(form)
        
    app.run(debug=True)

# Use Fire to run the script from the command line
if __name__ == '__main__':
    Fire({
        'md': md,
    })
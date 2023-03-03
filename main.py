from flask import Flask, request, jsonify, render_template
from quantum_app.config import qubit_db

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Landing page
    """
    try:
        return render_template('index.html')
    except Exception as e:
        return str(e)

@app.route('/job', methods=['POST'])
def submit_job():
    job = request.form.get('rotation')
    return "job is {}".format(job)
    if not job:
        return jsonify({'error': 'No job provided.'}), 400

    # Insert the job into the database
    job_id = qubit_db.jobs.insert_one({'job': job, 'status': 'pending'}).inserted_id

    # Add the job ID to the job queue
    qubit_db.job_queue.insert_one({'job_id': job_id})

    return jsonify({'job_id': str(job_id)}), 200

def validate_job_syntax(job):
    # TODO: Implement a function to validate the job syntax
    return True




if __name__ == '__main__':
    app.run()


import math
from random import random

from quantum_app.config import qubit_db


class QuantJob(object):
    """
    An object to recieve sequential rotations and execute the job
    """
    def __init__(self, job):
        """
        constructor
        """
        self.job = job

    # Define the X, Y, and Z gates
    @staticmethod
    def x(theta):
        return [[math.cos(theta/2), -1j*math.sin(theta/2)], [-1j*math.sin(theta/2), math.cos(theta/2)]]

    @staticmethod
    def y(theta):
        return [[math.cos(theta/2), -math.sin(theta/2)], [math.sin(theta/2), math.cos(theta/2)]]

    @staticmethod
    def z(theta):
        return [[math.exp(-1j*theta/2), 0], [0, math.exp(1j*theta/2)]]

    # Parse the string of rotations and execute them in sequence
    def qubit_run(self):
        rotations = self.job.split(", ")
        qubit_state = [[1, 0]]  # initial state: |0>
        for rotation in rotations:
            axis, angle_str = rotation.split("(")
            angle = int(angle_str[:-1])
            if axis == "X":
                gate = self.x(angle)
            elif axis == "Y":
                gate = self.y(angle)
            elif axis == "Z":
                gate = self.y(angle)
            else:
                raise ValueError("Invalid axis: {}".format(axis))
            qubit_state = self.matrix_mult(gate, qubit_state)
        bit = self.measure(qubit_state)
        return bit
    def execute_job(self):
        #Get the next job from the queue
        job = qubit_db.jobs.find_one({'status':'pending'})
        if not job:
            return
        qubit_db.jobs.update_one({'_id': job['_id']}, {'$set': {'status': 'running'}})
        self.qubit_run()
        # Update the job status to "completed"
        qubit_db.jobs.update_one({'_id': job['_id']}, {'$set': {'status': 'completed'}})

    # Measure a qubit state and return response or error code
    @staticmethod
    def measure(state):
        probabilities = [abs(coeff) ** 2 for coeff in state]
        cumulative_probs = [sum(probabilities[:i + 1]) for i in range(len(probabilities))]
        rand = random.random()
        return 0 if rand < cumulative_probs[0] else 1

    # Multiply two matrices (lists of lists)
    @staticmethod
    def matrix_mult(mat1, mat2):
        return [[sum(mat1[i][k] * mat2[k][j] for k in range(len(mat2))) for j in range(len(mat2[0]))] for i in range(len(mat1))]

    


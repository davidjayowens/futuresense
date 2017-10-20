from futuresense import FutureSense
import ast
from concurrent import futures
import pymongo

with open('users.csv', 'r') as f:
    users = ast.literal_eval(f.read())
users = users.keys()
users.remove('sandbox8')

def get_data(user):
    fs = FutureSense(user=user, sandbox=True)
    fs.get_all(all_reps=4)

for _ in xrange(13):
    executor = futures.ThreadPoolExecutor(10)
    future = [executor.submit(get_data, user)
                for user in users]
    futures.wait(future)

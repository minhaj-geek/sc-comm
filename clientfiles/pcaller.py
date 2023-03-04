'''
How to run Python file  from another python file
https://stackoverflow.com/questions/7974849/how-can-i-make-one-python-file-run-another
'''


from subprocess import call

while True:
        call(["python3", "pclient.py"])

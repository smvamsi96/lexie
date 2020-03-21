bind = "192.168.55.105:9000"                   # Don't use port 80 becaue nginx occupied it already. 
errorlog = '/Users/smvamsi/Code/logs/gunicorn-error.log'  # Make sure you have the log folder create
accesslog = '/Users/smvamsi/Code/logs/gunicorn-access.log'
loglevel = 'debug'
workers = 1     # the number of recommended workers is '2 * number of CPUs + 1' 


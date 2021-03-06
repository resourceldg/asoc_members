bind = '0.0.0.0:8000'
# Assuming one CPU. http://docs.gunicorn.org/en/stable/design.html#how-many-workers
# 2 * cores + 1
workers = 3
# You can send signals to it http://docs.gunicorn.org/en/latest/signals.html
pidfile = '/run/gunicorn.pid'
# Logformat including request time.
access_log_format = '%(h)s %({X-Forwarded-For}i)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" "%(L)s seconds"'  # noqa
loglevel = 'info'
accesslog = '-'  # stdout
errorlog = '-'  # stdout
# Also send logs to syslog.
syslog = False
syslog_prefix = '[asoc_members-wsgi]'
timeout = 84000

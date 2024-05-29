workers = 1
threads = 1
timeout = 120
accesslog = "-"
access_log_format = "url=%(r)s status_code=%(s)s agent=%(a)s request_time=%(M)sms"
errorlog = "-"
bind = "0.0.0.0:8000"

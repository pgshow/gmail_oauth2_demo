import yagmail

# 必须用海外VPS才能成功，否则SSL会报错
yag = yagmail.SMTP("sgdailydata@gmail.com", oauth2_file="./credentials.json")

subject = 'This is obviously the subject'
body = 'This is obviously the body'
html = '<a href="https://pypi.python.org/pypi/sky/">Click me!</a>'
img = '/local/file/bunny.png'

yag.send(to="target@gmail.com", subject=subject, contents=body)

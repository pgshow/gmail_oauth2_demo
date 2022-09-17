from yagmail import SMTP
# 必须用海外VPS才能成功，否则SSL会报错
conn = SMTP("sgdailydata@gmail.com", oauth2_file="./credentials.json")
conn.send(subject="It works!")

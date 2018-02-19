#!/usr/bin/python3

import twitter # βιβλιοθήκη python-twitter
import re,os
api = twitter.Api(consumer_key='HFF4kQRJXHUh0aDheI8EnD3lU',
  consumer_secret='MbAkrYen4zmyHZSFjdvkZztHiAX9WNddhQQtp7tbvNVxzQdhjf',
  access_token_key='2182632584-A3DLA18xzlOziLKnfgTyJaUIgpbyq8OWksbJBVM',
  access_token_secret='Y3pW3fUAlXIsH0YdmpIVfewtcX1qvE86Vxn6sdwcyrOQs')

#Φτιάχνει αρχείο με τα τελευταία 10 tweets
def creater(name):
    temp = open("twe","w+")
    try:
        t = api.GetUserTimeline(screen_name=name, count=10)
        tweets = [i.AsDict() for i in t]
        for g in tweets:
            temp.write(g['text']+ "\n")
        temp.close()
    except :
        print (name,":It does not exist that screen_name\n Give again the name:")
        main()

#Φτίαχνει dictionary με τις λέξεις που εχει χωρισει
def read():
    temp = open("twe","r")
    euretirio={}
    for i in temp:
        x = i.lower()
        x = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', " ",  x)#αφαιρει τα url
        words = re.sub("[^\w]", " ",  x).split()
        for word in words:
            if word in euretirio:
                euretirio[word] = euretirio[word] + 1
            else:
                euretirio[word] = 1
    return euretirio


#Βρίσκει το μέγιστο μεσα στο dictionary
def max_euretiriou(euretirio):
    max_times = max(euretirio.values())
    max_egrafes = [k for k, v in euretirio.items() if v == max_times]
    print("The most used words",max_egrafes,"Used",max_times,"times")

def main():
    name = input("Give the screen_name of twitter account (the one with '@'):")
    creater(name)
    euretirio = read()
    #max_euretiriou(euretirio)
    #os.remove("twe")

main()

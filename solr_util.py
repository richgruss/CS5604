import json
import httplib
import csv

def loadTwitterFile(file_name_in):
    count=0

    err = open('post_errors.txt','w')

    with open(file_name_in, 'rU') as csvfile:
         reader = csv.reader(csvfile, delimiter=',', quotechar='"')
         for line in reader:
            tweet = {'text': line[0], 'user_screen_name': line[1], 'id': line[2]}

            #print tweet
            #if count > 300:
            #    break
            #count = count+1
            try:
                post(tweet)
            except:
                err.write("Error on id: " + tweet['id'] + "\n")

    err.close()

def post(tweet):
    params = '['+json.dumps(tweet)+']'
    print "Posting: " + params
    headers = {"Content-type": "application/json",
           "Accept": "text/xml"}
    conn = httplib.HTTPConnection('localhost:8983')
    conn.request('POST', '/solr/collection1/update/json?commit=true', params, headers)
    response = conn.getresponse()
    print response.status, response.reason
    print "RESPONSE: " + response.read()
    conn.close()

def sq(str):
    return str[1:-1]

if __name__=='__main__':
    solr_dir = '/opt/solr/current'
    twitter_file_name =  'z_542_qp.csv'
    loadTwitterFile(twitter_file_name)

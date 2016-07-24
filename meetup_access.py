import meetup.api
import time

#Appel du client de l'API
 
client = meetup.api.Client('your_API_number', overlimit_wait=False)

rl = meetup.api.RateLimit


print rl.limit
print rl.remaining

x = client.GetMembers({'group_urlname' :'cultiver-autrement-des-legumes-a-paris'})

#ensemble des donnees sur les utilisateurs du groupe meetup.

def mudb(x=x, num = 0) :
	# print 'num', num
	num, mulist = 0, []
	for i in x.results :
		num = num + 1
		#liste de donnees par utilisateur du groupe meetup :
		mudb = {'num' : num, 'status' : i['status'].encode('UTF-8'), \
				'name' : i['name'].encode('UTF-8'), 'cities' : i['city'].encode('UTF-8'), \
				'country' : i['country'].encode('UTF-8'), \
				'id' : i['id'], 'joined' : i['joined']}
		mulist.append(mudb)
	return mulist

#liste du l'ensemble des villes ou habites les membres
#du groupe meetup.

def b(x=x) :
	vl = []
	for i in x.results :
		if i['city'].encode('UTF-8') not in vl :
			vl.append(i['city'].encode('UTF-8'))
		else :
			pass
	return vl

#liste de nom de l'ensemble des sujets auxquelles l'utilisateur 
#s'est inscrit.

def c(x=x):

	num, topics_l = 0, []
	for i in x.results :
		num = num + 1
		topics_list = []
		for j in i['topics'] :
			topics_list.append(j['name'])
		tdb = {'num' : num, 'nbr_of_topics' : len(topics_list), 'topics_list' : topics_list}
		topics_l.append(tdb)
	return topics_l

#liste de l'ensemble des "topics" par utilisateur du groupe meetup.

def d(x=x) :

	topics_l = c()
	unique_topics_list = []
	for i in x.results :
		for h in topics_l : 
			if h not in unique_topics_list : 
				#print h
				unique_topics_list.append(h)
	return unique_topics_list

#liste complete par utilisateur du groupe meetup.

def mulist() :
    
    mulist = []
    num = 0
    for i in c():
        num = num + 1
    #    print "--------------------"
    #    print "id_nbr :", num, i
        for j in mudb() :
            if i['num'] == j['num'] :
    #            print j, '\n'
                print 'i :', i['num'], 'c :', j['num']
    #            j.pop('num', 0)
                i.update(j)
#                print 'new_i :', i, '\n'
                if i not in mulist :
                    mulist.append(i)
#                    time.sleep(60)
                else :
                    pass 
    return mulist

#for i in mulist() :
#    print i['topics_list'], '\n'

if __name__ == "__main__" : 
    
    l = mulist()
    print l


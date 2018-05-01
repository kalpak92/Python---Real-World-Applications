def eg3_for(keys, values):
    dic = {}
    for i in range(len(keys)):
        dic[keys[i]] = values[i]
    return dic

def eg3_lc(keys, values):
    return { keys[i] : values[i] for i in range(len(keys)) }


country = ['India', 'Pakistan', 'Nepal', 'Bhutan', 'China', 'Bangladesh']
capital = ['New Delhi', 'Islamabad','Kathmandu', 'Thimphu', 'Beijing', 'Dhaka']
print ("FOR-loop result: " + str(eg3_for(country, capital)))
print ("LC result      : " + str(eg3_lc(country, capital)))

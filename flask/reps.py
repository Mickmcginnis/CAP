import json
import os
import jextract as extr
# curl "https://api.propublica.org/congress/v1/116/house/members.json" -H "X-API-Key: XirFDDm7LM9fETZWMhDCVhgOdWoVT881LVI3szQg" >> output.json
propdata = json.load(open('flask/output.json', 'r'))
members = propdata["members"]

def flatten(l):
    flatten_list = []
    for subl in l:
        for item in subl:
            flatten_list.append(item)
    return flatten_list

last_name = flatten((extr.extract_element_from_json(members, ["last_name"])))
first_name = flatten(extr.extract_element_from_json(members, ["first_name"]))
states = flatten((extr.extract_element_from_json(members, ["state"])))
districts = flatten((extr.extract_element_from_json(members, ["district"])))
gov_url = flatten((extr.extract_element_from_json(members, ["url"])))
parties = flatten((extr.extract_element_from_json(members, ["party"])))
states_abbr = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
            "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
            "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
            "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
            "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

def get_names():
    i=0
    names = []
    for member in members:
        fn = first_name[i]
        ln = last_name[i]
        names.append("{} {}".format(fn, ln))
        i+=1
    return names

def get_first_last():
    i=0
    names = []
    for item in last_name:
        ln = last_name[i]
        last_plus = ln.replace(" ", "+")
        names.append("{}+{}".format(first_name[i], last_plus))
        i+=1
    return names

rep_urls_list = get_first_last()

def get_party():
    i=0
    l=[]
    for item in last_name:
        party = parties[i]
        if party == "R":
            l.append("Republican")
        elif party == "D":
            l.append("Democrat")
        elif party == "I":
            l.append("Independent")
        i+=1
    return l

# recent votes
###################
# top donors

def find_by_name(spec_name):
    party = get_party()
    all_urls = get_first_last()
    k = all_urls.index(spec_name)
    fn1 = first_name[k]
    ln1 = last_name[k]
    p = party[k]
    s1 = states[k]
    d1 = districts[k]
    gu1 = gov_url[k]
    l=[fn1, ln1, p, s1, d1, gu1]
    return l

def get_by_state():
    r_by_state = []
    for s in states_abbr:
        slist = []
        fl = get_first_last()
        for r in fl:
            r_info = find_by_name(r)
            if r_info[3] == s:
                fn = r_info[0]
                ln = r_info[1]
                slist.append("{} {}".format(fn, ln))
        r_by_state.append(slist)
    print(r_by_state)
    return r_by_state

reps_by_state = get_by_state()

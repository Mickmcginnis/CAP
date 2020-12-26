# committees
import json

committee_mem_data = json.load(open('committee_membership.json', 'r'))

committees_abbr = ["HLIG","HSAG","HSAP","HSAS","HSBA","HSBU","HSED","HSFA","HSGO","HSHA","HSHM","HSIF","HSII","HSJU","HSPW","HSRU","HSSM","HSSO","HSSY","HSVR","HSWM","JCSE","JSEC","JSLC","JSPR","JSTX","HSCN","HSMH"]

def flatten(l):
    flatten_list = []
    for subl in l:
        for item in subl:
            flatten_list.append(item)
    return flatten_list

def get_committee_mems():
    for item in committees_abbr:
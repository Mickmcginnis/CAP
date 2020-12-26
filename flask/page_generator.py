from jinja2 import Environment, FileSystemLoader
from flask import Flask
from flask import render_template, current_app, request, Response, redirect, url_for, session
import reps

reps_list = reps.get_names()
reps_urls = reps.get_first_last()

def gen_pages(rep=None):
    output = render_template(
        'house.html', 
        rep=rep, 
        reps_list=reps_list,
        reps_urls=reps_urls
        )
    return output

def gen_page(rep):
    rep_info = reps.find_by_name(rep)
    first_name = rep_info[0]
    last_name = rep_info[1]
    party = rep_info[2]
    state = rep_info[3]
    district = rep_info[4]
    gov_url = rep_info[5]
    output = render_template(
        'page.html', 
        rep=rep, 
        first_name=first_name,
        last_name=last_name,
        party=party,
        state=state,
        district=district,
        gov_url=gov_url
        )
    return output
import json
from random import randint
import numpy as np
import pandas as pd


def offers_generate():
    offers_file  = open("data.json").read()
    tags_file = open("tags.json").read()


    offers = json.loads(offers_file)
    tags = json.loads(tags_file)

    for offer in offers:
        for i in range(10):
            tag_key = randint(0, len(tags) -1)
            offer['tag'].append(tags[tag_key])
            # print(offer)
    return offers

def score_tags(tags_s, tags):
    
    score = 0

    for tag_s in tags_s:
        for tag in tags:
            if tag_s == tag:
                score+=1

    return score

def offer_analyse(offer, offers):
    scores = []
    offersId = []
    
    for offer_p in offers:
        if offer_p == offer:
            continue
        score = score_tags(offer['tag'], offer_p['tag'])
        scores.append(score)
        offersId.append(offer_p['id']['$oid'])


    dfScore = pd.DataFrame({
        "scores": scores,
        "offers": offersId
    })

    return dfScore

offers = offers_generate()

offer = offers[randint(0, len(offers) -1)]
scores_offer = offer_analyse(offer, offers)

print(scores_offer.sort_values(by=['scores'], ascending=False))

let offers = require("./dataGenerate")();

function  generateList(offer){
    
}

async function analyseTags(offerSelected, offers){
    let scores = []
    
    await offers.map(offer => {
        let score = scoreTag(offerSelected.tag, offer.tag);

        scores.push([score, offer.id.$oid]);
    })

    return scores;
}

async function scoreTag(tagsSelected, tags){
    
    let score = 0;

    await tagsSelected.forEach(tagS => {
        tags.forEach(tag => {
            if(tag == tagS)
                score++;
        })
    })

    return score;
}


console.log(offers);
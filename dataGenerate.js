const fs = require("fs");
const TAGS_PER_OFFER = 10;

module.exports = () => {
        var offers = JSON.parse(fs.readFileSync('data.json', 'utf8'));
        var tags = JSON.parse(fs.readFileSync('tags.json', 'utf8'));

        

        for(offer in offers){
            for(let i = 0; i < TAGS_PER_OFFER; i ++){
                
                let tagIndex = Math.floor(Math.random() * (tags.length - 1));
                
                offers[offer].tag.push(tags[tagIndex])
            }
        }

        return offers;
    }



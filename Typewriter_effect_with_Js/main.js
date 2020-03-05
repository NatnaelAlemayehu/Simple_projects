// const TypeWriter = function (txtElement, words, wait = 3000) {
//     this.txtElement = txtElement;
//     console.log(txtElement)
//     this.words = words;
//     console.log(words);
//     this.txt = '';
//     this.wordIndex = 0;
//     this.wait = parseInt(wait, 10);
//     this.type();
//     this.isDeleting = false;
// }

// //Type Method
// TypeWriter.prototype.type = function () {
//     //current index of word
//     const current = this.wordIndex % this.words.length;
//     //Get full text of current word
//     const fullTxt = this.words[current];

//     //check if deleting
//     if (this.isDeleting) {
//         this.txt = fullTxt.substring(0, this.txt.length - 1);
//     } else {
//         //Add character
//         this.txt = fullTxt.substring(0, this.txt.length + 1);
//     }
//     //Insert txt into element
//     this.txtElement.innerHTML = `<span class = "txt">${this.txt}</span>`;
    
//     //Initial Type speed
//     let typespeed = 300;
//     if (this.isDeleting) {
//         typespeed /= 2;
//     }
//     // if word is complete
//     if (!this.isDeleting && this.txt === fullTxt) {
//         //make pause at end
//         typespeed = this.wait;
//         this.isDeleting = true;
//     } else if (this.isDeleting && this.txt === '') {
//         this.isDeleting = false;
//         //move to the next word
//         this.wordIndex++;
//         //pause before start typing
//         typespeed = 500;
//     }
//     setTimeout(() => this.type(), typespeed);
// }


class TypeWriter{
    constructor(txtElement, words, wait) {
        this.txtElement = txtElement;
        this.words = words;
        this.txt = '';
        this.wordIndex = 0;
        this.wait = parseInt(wait, 10);
        this.isDeleting = false;
        this.type();
        this.cursor();
    }
    type() {
        //current index of word
        const current = this.wordIndex % this.words.length;
        //Get full text of current word
        const fullTxt = this.words[current];

        //check if deleting
        if (this.isDeleting) {
            this.txt = fullTxt.substring(0, this.txt.length - 1);
        } else {
            //Add character
            this.txt = fullTxt.substring(0, this.txt.length + 1);
        }
        //Insert txt into element
        this.txtElement.innerHTML = `<span class = "txt">${this.txt}<span id = "cursor">|</span></span>`;

        //Initial Type speed
        let typespeed = 300;
        if (this.isDeleting) {
            typespeed /= 2;
        }
        // if word is complete
        if (!this.isDeleting && this.txt === fullTxt) {
            //make pause at end
            typespeed = this.wait;
            this.isDeleting = true;
        } else if (this.isDeleting && this.txt === '') {
            this.isDeleting = false;
            //move to the next word
            this.wordIndex++;
            //pause before start typing
            typespeed = 500;
        }
        setTimeout(() => this.type(), typespeed);  
    }
    cursor() {
        var cursor = true;
        setInterval(() => {
            if (cursor) {
                document.getElementById('cursor').style.opacity = 0;
                cursor = false;
            } else {
                document.getElementById('cursor').style.opacity = 1;
                cursor = true;
            }
        }, 300);
    }

}

// Init On DOM Load
document.addEventListener('DOMContentLoaded', init);

function init() {
    const txtElement = document.querySelector('.txt-type');
    console.log(txtElement);
    const words = JSON.parse(txtElement.getAttribute('data-words'));
    // const words = txtElement.getAttribute('data-words'); 

    const wait = txtElement.getAttribute('data-wait');
    new TypeWriter(txtElement, words, wait);
}


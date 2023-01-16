// Adds a transition delay and a class to cause a cool animation
function reveal(){

    // Find the hidden cards
    var cards = $('div.card.hidden')

    // Add transition delay for each hidden card
    var count = 0
    for(var card of cards){
        var delay = (count * 200) + "ms"
        $(card).css('transition-delay', delay)
        count++
    }

    // Add the show class to each card to animate them
    for(var card of cards){
        $(card).addClass('show')
        console.log(card)
    }
}

// When document is ready, call the reveal function
$('document').ready(reveal)
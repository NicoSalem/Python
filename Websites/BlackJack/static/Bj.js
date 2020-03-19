var deck = 9;
var playerSum = 0;
var dealerSum = 0;
var playerCard1 = 0;
var playerCard2 = 0;
var cardReturn;
var cash = 50;
var round_over = false;

let card_value_map = new Map();
card_value_map.set("2", 2);card_value_map.set("3", 3);card_value_map.set("4", 4);
card_value_map.set("5", 5);card_value_map.set("6", 6);card_value_map.set("7", 7);
card_value_map.set("8", 8);card_value_map.set("9", 9);card_value_map.set("10", 10);
card_value_map.set("JACK", 10);card_value_map.set("QUEEN", 10);card_value_map.set("KING", 10);card_value_map.set("ACE", 11);

  
window.onload = function()
{
    var hitbtn = document.getElementsByTagName("button")[0];
    hitbtn.onclick = function()
    {
        if(playerSum!=0 && playerSum<=21 && round_over==false){get_P_Card();}
    }

    var standtbn = document.getElementsByTagName("button")[1];
    standtbn.onclick = function Stand()
    {
        if(dealerSum!=0 && round_over==false)
        {
            // Dealer starts playing
            
            while(dealerSum<17)
            { 
                get_D_Card();
            }
            

            if(dealerSum>21 || (playerSum > dealerSum && playerSum <=21))
            {
                cash+=5; document.getElementById("cash").innerHTML = cash;
                
                document.getElementById("prompt").innerHTML = "you won";
                document.getElementById("prompt").setAttribute("style","color:cyan");
                round_over = true;
                if(cash<=0){document.getElementById("prompt").innerHTML = "you lost all your money";
                document.getElementById("prompt").setAttribute("style","color:red");}

                else 
                {
                    console.log("right");
                    var nb = document.getElementById("nrb");
                    var btn = document.createElement("button");
                    btn.setAttribute("style", "height: 3vh");
                    var btntxt = document.createTextNode("Another round");
                    btn.appendChild(btntxt);
                    nb.appendChild(btn);
                    nb.onclick = function()
                    {
                        if(round_over==true)
                        {
                            Clear_for_next_round();
                            round();
                        }
                    }
                }
                
            }
            else
            {
                cash-=5; document.getElementById("cash").innerHTML = cash;
                
                document.getElementById("prompt").innerHTML = "Dealer won";
                document.getElementById("prompt").setAttribute("style","color:red");
                round_over = true;
                if(cash<=0){document.getElementById("prompt").innerHTML = "you lost all your money";
                document.getElementById("prompt").setAttribute("style","color:red");}

                else 
                {
                    console.log("right");
                    var nb = document.getElementById("nrb");
                    var btn = document.createElement("button");
                    btn.setAttribute("style", "height: 3vh");
                    var btntxt = document.createTextNode("Another round");
                    btn.appendChild(btntxt);
                    nb.appendChild(btn);
                    nb.onclick = function()
                    {
                        if(round_over==true)
                        {
                            Clear_for_next_round();
                            round();
                        }
                    }
                }
                
            }
        }

    }

    var doublebtn = document.getElementsByTagName("button")[2];
    doublebtn.onclick = function double()
    {
    
    }

    var splitbtn = document.getElementsByTagName("button")[3];
    splitbtn.onclick = function split()
    {
    
    }

    this.round();
    
    
    
    if(cash==0)
    {
        console.log("you lost all your money :(");
    }

    

}

function round()
{
    this.getDeck();
    document.getElementById("cash").appendChild(this.document.createTextNode(cash));
    playerCard1 = get_P_Card();
    get_D_Card();
    playerCard2 = get_P_Card();
}

function getDeck()
{
    var xmlhttp = new XMLHttpRequest();
    
    xmlhttp.onreadystatechange = function() 
    {
        if (this.readyState == 4 && this.status == 200)
         {
            var response = JSON.parse(this.responseText);
            deck = response.deck_id;
        }
    };

    xmlhttp.open("GET", "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=6", false);
    xmlhttp.send();
    console.log(deck);
}

function get_D_Card()
{
    var xmlhttp = new XMLHttpRequest(); 
    
    xmlhttp.onreadystatechange = function() 
    {
        if (this.readyState == 4 && this.status == 200)
         {
            var card = JSON.parse(this.responseText);
            console.log("dealersum: "+ dealerSum);
            var card_img_src = card.cards[0].image;
            var div = document.getElementById("dealer");
            var new_img = document.createElement("img");
            new_img.setAttribute("style", "height: 20vh; width: 10vw;");
            new_img.setAttribute("src", card_img_src);
            div.appendChild(new_img);  
            dealerSum += card_value_map.get(card.cards[0].value);          
        }
    };

    xmlhttp.open("GET", "https://deckofcardsapi.com/api/deck/"+deck+"/draw/?count=1", false);
    xmlhttp.send();

}

function get_P_Card()
{
    var xmlhttp = new XMLHttpRequest();
    
    xmlhttp.onreadystatechange = function() 
    {
        if (this.readyState == 4 && this.status == 200)
         {
            var card = JSON.parse(this.responseText);
            playerSum += card_value_map.get(card.cards[0].value);

            if(playerSum > 21)
            {
                round_over = true;
                console.log("playersum: "+playerSum);
                cardReturn = card_value_map.get(card.cards[0].value);
                var card_img_src = card.cards[0].image;
                var div = document.getElementById("player");
                var new_img = document.createElement("img");
                new_img.setAttribute("style", "height: 20vh; width: 10vw;");
                new_img.setAttribute("src", card_img_src);
                div.appendChild(new_img);
                
                cash-=5; document.getElementById("cash").innerHTML = cash;

                document.getElementById("prompt").innerHTML = "you burned";
                document.getElementById("prompt").setAttribute("style","color:red");

                if(cash<=0){document.getElementById("prompt").innerHTML = "you lost all your money";
                document.getElementById("prompt").setAttribute("style","color:red");}
                
                else 
                {
                    console.log("right");
                    var nb = document.getElementById("nrb");
                    var btn = document.createElement("button");
                    btn.setAttribute("style", "height: 3vh");
                    var btntxt = document.createTextNode("Another round");
                    btn.appendChild(btntxt);
                    nb.appendChild(btn);
                    nb.onclick = function()
                    {
                        if(round_over==true)
                        {
                            Clear_for_next_round();
                            round();
                        }
                    }
                }
                
            }
            else
            {
                console.log("playersum: "+playerSum);
                cardReturn = card_value_map.get(card.cards[0].value);
                var card_img_src = card.cards[0].image;
                var div = document.getElementById("player");
                var new_img = document.createElement("img");
                new_img.setAttribute("style", "height: 20vh; width: 10vw;");
                new_img.setAttribute("src", card_img_src);
                div.appendChild(new_img);
            }
        }
    };

    xmlhttp.open("GET", "https://deckofcardsapi.com/api/deck/"+deck+"/draw/?count=1", false);
    xmlhttp.send();

    return cardReturn;
}

function Clear_for_next_round()
{
    playerSum = 0;
    dealerSum = 0;
    document.getElementById("cash").innerHTML = "";
    var pdiv = document.getElementById("player");
    var child = pdiv.lastElementChild; 

    while (child)
    { 
        pdiv.removeChild(child); 
        child = pdiv.lastElementChild; 
    } 
    
    var ddiv = document.getElementById("dealer");
    var child = ddiv.lastElementChild;  
    while (child) 
    { 
        ddiv.removeChild(child); 
        child = ddiv.lastElementChild; 
    } 
    var p = document.getElementById("prompt").innerHTML = "";
    document.getElementById("nrb").removeChild(document.getElementById("nrb").lastElementChild);
    
    round_over = false;
}







window.onload = function()
{
    var bodytag = document.getElementsByTagName("body")[0];
    var bjButton = document.getElementsByTagName("button")[0];


    console.log("Loaded");

    bjButton.onclick = function()
    {
        window.open("/BlackJack", "_self");
        console.log("Click");
    };

    
    
}

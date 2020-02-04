var bodytag = document.getElementsByTagName("body")[0];
var button = document.getElementsByTagName("button")[0];
var jtitle = document.getElementsByTagName("input")[0];
var jlocation = document.getElementsByTagName("input")[1];

window.onload = function()
{

    var nsp = io.connect();
    document.getElementsByTagName("button")[0].onclick = function(){
            
            
        console.log(document.getElementsByTagName("input")[0].value);
        nsp.emit('emit1', document.getElementsByTagName("input")[0].value);
        window.open("locations", "_self")
        // var frame = document.getElementsById("frame")
        // frame.src = frame.src
        
    };

    // nsp.on("emit1")
    // {
    //     document.getElementsByTagName("iframe")[0].contentWindow.location.reload();
    // }

}


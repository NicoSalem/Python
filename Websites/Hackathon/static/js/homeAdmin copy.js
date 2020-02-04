// var fs = require('fs')

// var text = fs.readFileSync("../../coordinates.txt").toString()

// console.log(text);

// var s1 = text.split("\n")

// console.log(s1);

// console.log(s1[0])

// var s2 = s1[0].split(" ")
// console.log(s2[0])

var fs = require('fs')
var text = fs.readFileSync("../../coordinates.txt").toString()
var s1 = text.split("\n")
console.log(s1);
for(var line of s1)
{
    var co = line.split(" ");
    console.log(co[0]);
}

// var fs = require('fs')
// var text = fs.readFileSync("../../coordinates.txt").toString()
// var s1 = text.split("\n")
// for (line in s1)
// {
//     var marker = l.marker([line[0], line[1]]).addTo(map);
// }

// <!DOCTYPE html>
// <html>
// <head>
//     <link rel="stylesheet" href="https://unpkg.com/leaflet@1.5.1/dist/leaflet.css" />
//     <script src="https://unpkg.com/leaflet@1.5.1/dist/leaflet.js"></script>
//     <style>
//         #map {position: absolute; top:0; bottom: 0; left: 0; right: 0;}
//     </style>
// </head>
// <body>
//     <div id="map"></div>
//     <script>
//         var map = l.map('map').setView([0,0],1);
//         l.tileLayer('https://api.maptiler.com/maps/streets/256/tiles.json?key=4lKhxMvZUtW84W1uAFyy', 
//         {
//             attribution:'<a href="https://www.maptiler.com/copyright/" target="_blank">&copy; MapTiler</a> <a href="https://www.openstreetmap.org/copyright" target="_blank">&copy; OpenStreetMap contributors</a>'
//         }).addTo(map);
//     </script>
// </body>
// </html>

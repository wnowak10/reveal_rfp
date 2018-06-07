
 var grid = d3.select("body")
 	.append("div")
 	.attr("id", "grid")
 	.attr("class", "grid")

//////////////////////////////////////////
//////////////////////////////////////////
// Set globals
//////////////////////////////////////////
//////////////////////////////////////////
var current_county_id; 

var race = 'all';
var variable = 'Poverty';

var div = d3.select("body").append("div") 
    .attr("class", "tooltip")       
    .style("opacity", 0);
    
//////////////////////////////////////////
//////////////////////////////////////////
// Set the title.
//////////////////////////////////////////
//////////////////////////////////////////

var title_div = grid
    .append("div")
    .attr("class", "row_divs");

title_div.append("h1")
  .attr("id", "title_text")
    .text("POVERTY");

var sub_title_div = grid
    .append("div")
    .attr("class", "row_divs");

sub_title_div.append("h2")
  .attr("id", "subtitle_text")
    .text("THE POVERTY RATE VARIES DRAMATICALLY ACROSS DIFFERENT REGIONS OF THE COUNTRY, AS WELL.");




//////////////////////////////////////////
//////////////////////////////////////////
// Set the dimensions of the canvas/graph.
// Begin to make the map.
// //////////////////////////////////////////
// //////////////////////////////////////////
var margin = {top: 40, right: 20, bottom: 30, left: 50};
var width = 700;
var height = 350;
var mapHeight = 550;


var chart1 = grid.append("div").attr("class", "row_divs").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", mapHeight);

// This is a global var declared in reveal js
g = chart1.append("g");
console.log("g now", g)
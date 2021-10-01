// set the dimensions of the canvas
function bar(element, jsonData, xColumnName, yColumnName) {
    elementTop = $(element).position().top
    elementLeft = $(element).position().left
    elementHeight = $(element).height()
    elementWidth = $(element).width()

    // alert(elementLeft)
    var margin = { top: 50, right: 20, bottom: 70, left: 50 },
        width = elementWidth - 100,
        height = elementHeight - 50;


    // set the ranges
    var x = d3.scale.ordinal().rangeRoundBands([10, width], .05);

    var y = d3.scale.linear().range([height, 0]);

    // define the axis
    var xAxis = d3.svg.axis()
        .scale(x)
        .orient("bottom")


    var yAxis = d3.svg.axis()
        .scale(y)
        .orient("left")
        .ticks(10);

    
    // add the SVG element
    var svg = d3.select(element).append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");


    // load the data
    d3.json("empty.json", function (error, data) {

        // data.forEach(function(d) {
        //     d.Letter = d.Letter;
        //     d.Freq = +d.Freq;
        // });
        data = jsonData

        // scale the range of the data
        x.domain(data.map(function (d) { return d.dimensions; }));
        y.domain([0, d3.max(data, function (d) { return d.measure; })]);

        // add axis
        svg.append("g")
            .attr("class", "x axis")
            .attr("transform", "translate(0," + height + ")")
            .call(xAxis)
            .selectAll("text")
            .style("text-anchor", "end")
            .attr("dx", "-.8em")
            .attr("dy", "-.55em")
            .attr("transform", "rotate(-90)");

        svg.append("g")
            .attr("class", "y axis")
            .call(yAxis)
            .append("text")
            .attr("transform", "rotate(-90)")
            .attr("y", 5)
            .attr("dy", ".71em")
            .style("text-anchor", "end")
            .text(yColumnName);

        // Add bar chart
        svg.selectAll("bar")
            .data(data)
            .enter().append("rect")
            .attr("class", "bar")
            .attr("x", function (d) { return x(d.dimensions); })
            .attr("width", x.rangeBand())
            .attr("y", function (d) { return y(d.measure); })
            .attr("height", function (d) { return height - y(d.measure); });
        

    });
    function type(d) {
        d.measure = +d.measure;
        return d;
      }

}
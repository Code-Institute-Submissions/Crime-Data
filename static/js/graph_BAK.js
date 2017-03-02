/*queue()
    .defer(d3.json, "/stuff")
    .await(MakeGraphs);

function MakeGraphs(error, sourceJson) {
    var crime_DataSource = sourceJson;
    var dateFormat = d3.time.format("%Y-%m-%d %H:%M:%S");
    crime_DataSource.forEach(function (d) {
        d["date_posted"] = dateFormat.parse(d["date_posted"]);
        d["date_posted"].setDate(1);
        d["attempts or threats to murder, assaults, harassments and related offences 2004"] = +d["attempts or threats to murder, assaults, harassments and related offences 2004"];
    });

}*/




/*
* var ndx = crossfilter(crime_DataSource);

    var dateDim = ndx.dimension(function (d) {
        return d["date_posted"];
    });

    var attemps2004Dim = ndx.dimension(function (d) {
        return d["attempts_2004"];
    });

    var numSourceAttemps2004 = attemps2004Dim.group();

    var attempts2004Chart = dc.rowChart("#attempt-2004-row-chart");


    attempts2004Chart
        .width(300)
        .height(250)
        .dimension(attemps2004Dim)
        .group(numSourceAttemps2004)
        .xAxis().ticks(4);


    dc.renderAll();
*
* */
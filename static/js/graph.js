queue()
    .defer(d3.json, "/crime")
    .await(makeGraphs);

function makeGraphs(error, projectsJson) {


    //Clean projectsJson data
    var crime_DataProjects = projectsJson;
    var dateFormat = d3.time.format("%Y-%m-%d %H:%M:%S");
    crime_DataProjects.forEach(function (d) {
        d["Attempts or threats to murder, assaults, harassments and related offences 2004"] = +d["Attempts or threats to murder, assaults, harassments and related offences 2004"];
    });


    //Creating Crossfilter
    var ndx = crossfilter(crime_DataProjects);

    //Define Dimensions

    var countyDim = ndx.dimension(function(d){
        return d["County"]
    });

    var attempts2004Dim = ndx.dimension(function (d) {
        return d["Attempts or threats to murder, assaults, harassments and related offences 2004"];
    });

    var divisionsDim = ndx.dimension(function (d) {
        return d['Divisions']

    })


    //Calculate metrics
    var numCrimesByCounty = countyDim.group();
    var numProjectsAttempts2004 = attempts2004Dim.group();
    var numProjectsByDivision = divisionsDim.group();


    //Define values (to be used in charts)


    //Charts


    //var attemptsLevelChart = dc.rowChart("#attempts-2004-row-chart");


    var attemptsLevelChart = dc.rowChart("#attempts-2004-row-chart");

    var divisionPieChart = dc.pieChart("#test")

     selectField = dc.selectMenu('#menu-select')
       .dimension(countyDim)
       .group(numCrimesByCounty);

    attemptsLevelChart
        .width(900)
        .height(450)
        .dimension(attempts2004Dim)
        .group(numProjectsByDivision)
        .xAxis().ticks(10);

    divisionPieChart
      .height(500)
       .radius(410)
       .innerRadius(10)
       .transitionDuration(1500)
       .dimension(countyDim)
       .group(numProjectsAttempts2004);

    dc.renderAll();
}
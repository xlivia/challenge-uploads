// Read in samples.json from the provided URL
function readSamplesJSON() {
    let samplesUrlRead = "https://2u-data-curriculum-team.s3.amazonaws.com/dataviz-classroom/v1.1/14-Interactive-Web-Visualizations/02-Homework/samples.json";
    d3.json(samplesUrlRead).then((data) => {
        console.log("Samples JSON data:", data);
        // Call functions to create the charts and display metadata
        createBarChart(data);
        createBubbleChart(data);
        displayMetadata(data);
        createGaugeChart(data);
    }).catch(function(error) {
        console.log("Error reading samples.json:", error);
    });
}
// Create the horizontal bar chart
function createBarChart(data) {

    // Extract the top 10 OTUs for the selected individual
    let selectedValue = d3.select("#selDataset").property("value");
    let samples = data.samples.filter(sample => sample.id === selectedValue)[0];
    let otuIds = samples.otu_ids.slice(0, 10).map(id => `OTU ${id}`).reverse();
    let sampleValues = samples.sample_values.slice(0, 10).reverse();
    let otuLabels = samples.otu_labels.slice(0, 10).reverse();

    // Create the trace for the bar chart
    let trace = {
        x: sampleValues,
        y: otuIds,
        text: otuLabels,
        type: "bar",
        orientation: "h"
    };

    // Create the data array
    let chartData = [trace];

    // Define the layout
    let layout = {
        title: "Top 10 OTUs",
        xaxis: { title: "Sample Values" },
        yaxis: { title: "OTU IDs" }
    };

    // Plot the chart
    Plotly.newPlot("bar", chartData, layout);
}

// Create the bubble chart
function createBubbleChart(data) {

    // Extract the data for the selected individual
    let selectedValue = d3.select("#selDataset").property("value");
    let samples = data.samples.filter(sample => sample.id === selectedValue)[0];
    let otuIds = samples.otu_ids;
    let sampleValues = samples.sample_values;
    let otuLabels = samples.otu_labels;

    // Create the trace for the bubble chart
    let trace = {
        x: otuIds,
        y: sampleValues,
        text: otuLabels,
        mode: "markers",
        marker: {
            size: sampleValues,
            color: otuIds,
            colorscale: "Earth"
        }
    };

    // Create the data array
    let chartData = [trace];

    // Define the layout
    let layout = {
        title: "OTU Bubble Chart",
        xaxis: { title: "OTU IDs" },
        yaxis: { title: "Sample Values" }
    };

    // Plot the chart
    Plotly.newPlot("bubble", chartData, layout);
}

// Display the sample metadata
function displayMetadata(data) {
    // Get the metadata for the selected individual
    let selectedValue = d3.select("#selDataset").property("value");
    let metadata = data.metadata.filter(meta => meta.id.toString() === selectedValue)[0];

    // Clear any existing metadata
    d3.select("#sample-metadata").html("");

    // Loop through each key-value pair in the metadata and display it
    Object.entries(metadata).forEach(([key, value]) => {
        d3.select("#sample-metadata").append("p").text(`${key}: ${value}`);
    });
}

// Update all the plots and metadata when a new sample is selected
function optionChanged(selectedValue) {
    console.log("Selected value:", selectedValue);
    readSamplesJSON().then(data => {
        createBarChart(data, selectedValue);
        createBubbleChart(data, selectedValue);
        displayMetadata(data, selectedValue);
        updateGaugeChart(selectedValue);
    });
}

// Function to initialize the page
function init() {
    console.log("Initializing the page...");
    let samplesUrlInit = "https://2u-data-curriculum-team.s3.amazonaws.com/dataviz-classroom/v1.1/14-Interactive-Web-Visualizations/02-Homework/samples.json";
    // Populate the dropdown menu
    d3.json(samplesUrlInit).then(function(data) {
        // Get the IDs of all individuals
        let ids = data.names;
        // Populate the dropdown menu with options
        let dropdown = d3.select("#selDataset");
        ids.forEach(function(id) {
            dropdown.append("option").text(id).property("value", id);
        });
        // Call the function to read the samples.json data
        readSamplesJSON();
    }).catch(function(error) {
        console.log("Error reading samples.json:", error);
    });
    console.log("Initializing the page...");
}

// Call the init function to initialize the page
init();
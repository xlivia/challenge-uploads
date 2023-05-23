// Create the gauge chart
function createGaugeChart(data) {
    // Extract the washing frequency for the selected individual
    let selectedValue = d3.select("#selDataset").property("value");
    let metadata = data.metadata.filter((meta) => meta.id.toString() === selectedValue)[0];
    let washingFreq = metadata.wfreq;
    // Create the trace for the gauge chart
    let trace = {
        type: "indicator",
        mode: "gauge+number",
        value: washingFreq,
        title: {
            text: "<b>Belly Button Washing Frequency</b><br>Scrubs per Week",
            font: { size: 24 }
        },
        gauge: {
            axis: { range: [0, 9] },
            bar: { color: "#1f77b4" },
            steps: [
                { range: [0, 3], color: "#ebedf0" },
                { range: [3, 6], color: "#c6dbef" },
                { range: [6, 9], color: "#9ecae1" },
            ],
            threshold: {
                line: { color: "red", width: 4 },
                thickness: 0.75,
                value: washingFreq,
            },
        },
    };
    // Create the data array
    let chartData = [trace];
    // Define the layout
    let layout = {
        width: 500,
        height: 400,
        margin: { t: 0, b: 0 },
    };
    // Plot the chart
    Plotly.newPlot("gauge", chartData, layout);
}

// Update the gauge chart whenever a new sample is selected
function updateGaugeChart(selectedValue) {
    d3.json("samples.json").then((data) => {
        let wfreq = data.metadata.filter((meta) => meta.id.toString() === selectedValue)[0].wfreq;
        createGaugeChart(wfreq);
    }).catch(function (error) {
        console.log("Error reading samples.json:", error);
    });
}

// Call the updateGaugeChart function to display the gauge chart onload
updateGaugeChart(selectedValue);
console.log("script")
let states;

// This code will execute on page load to populate the dropdown
d3.json("/api/alldata").then(function(data) {
  // Create a set to store unique states
  let uniqueStates = new Set(data.map(item => item.state));
  
  // Convert the set back to an array
  states = [...uniqueStates];
  
  console.log(states);
  for(let state of states) {
    d3.select("#selDataset").append("option").attr("value", state).text(state);
  }
});

// Function definition that will be called with select event change handler
function optionChanged(state) {
  console.log(state); // Check what value is being passed
  
  // Ensure the state abbreviation is valid before proceeding
  if (typeof state === 'string' && state.length === 2) {
    // Fetch data for the selected state
    d3.json(`/api/stateavg/${state}`).then(function(data) {
      console.log(data); // Log the fetched data for debugging

      // Extract years and rent values from the data
      let years = data.map(d => d.year);
      let avgStudio = data.map(d => d.avg_studio);
      let avgOneBedroom = data.map(d => d.avg_one_bedroom);
      let avgTwoBedroom = data.map(d => d.avg_two_bedroom);
      let avgThreeBedroom = data.map(d => d.avg_three_bedroom);
      let avgFourBedroom = data.map(d => d.avg_four_bedroom);

      // Define traces for Plotly
      let trace1 = {
        x: years,
        y: avgStudio,
        mode: 'lines+markers',
        name: 'Avg Studio Rent'
      };
      let trace2 = {
        x: years,
        y: avgOneBedroom,
        mode: 'lines+markers',
        name: 'Avg One Bedroom Rent'
      };
      let trace3 = {
        x: years,
        y: avgTwoBedroom,
        mode: 'lines+markers',
        name: 'Avg Two Bedroom Rent'
      };
      let trace4 = {
        x: years,
        y: avgThreeBedroom,
        mode: 'lines+markers',
        name: 'Avg Three Bedroom Rent'
      };
      let trace5 = {
        x: years,
        y: avgFourBedroom,
        mode: 'lines+markers',
        name: 'Avg Four Bedroom Rent'
      };

      // Plot the graph
      let dataToPlot = [trace1, trace2, trace3, trace4, trace5];
      let layout = {
        title: `Average Rent Prices in ${state}`,
        xaxis: { title: 'Year' },
        yaxis: { title: 'Average Rent Price' }
      };

      Plotly.newPlot('chart', dataToPlot, layout);
    }).catch(error => {
      console.error('Error fetching data:', error);
    });
  } else {
    console.error('Invalid state abbreviation:', state);
  }
}

// Initialize the default plot with studio data
optionChanged('AZ');
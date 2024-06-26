console.log("script");

// Function to handle the bedroom dropdown change event
function bedroomOptionChanged(bedrooms) {
  console.log(bedrooms); // Check what value is being passed

  // Fetch data for the selected number of bedrooms
  d3.json(`/api/rentdollarchange?bedrooms=${bedrooms}`).then(function(data) {
    console.log(data); // Log the fetched data for debugging

    // Extract states and rent dollar changes from the data
    let states = data.map(d => d.state);
    let rentDollarChanges = data.map(d => d.rent_dollar_change);

    // Combine states and rent dollar changes into an array of objects
    let combinedData = states.map((state, index) => {
      return { state: state, rent_dollar_change: rentDollarChanges[index] };
    });

    // Sort the combined data by rent dollar change in ascending order
    combinedData.sort((a, b) => a.rent_dollar_change - b.rent_dollar_change);

    // Separate the sorted data back into states and rent dollar changes
    let sortedStates = combinedData.map(d => d.state);
    let sortedRentDollarChanges = combinedData.map(d => d.rent_dollar_change);

    // Define traces for Plotly
    let trace = {
      x: sortedStates,
      y: sortedRentDollarChanges,
      type: 'bar'
    };

    // Plot the bar chart
    let dataToPlot = [trace];
    let layout = {
      title: `Changes in Rent Prices of ${bedrooms.replace('_', ' ').capitalize()}s`,
      xaxis: { 
        title: 'State',
        tickangle: -45, // Rotate x-axis labels
        automargin: true, // Automatically adjust margins to prevent label overlap
        tickfont: {
          size: 10 // Make x-axis labels smaller
        }
      },
      yaxis: { title: 'Change in Rent Price',
      tickformat: '$,.0f' // Format the y-axis labels in $0,00 format
      },
      margin: {
        t: 50, // Top margin
        b: 150 // Bottom margin to accommodate the rotated labels
      },
      width: 1400 // Increase the width of the chart
    };

    Plotly.newPlot('barChart', dataToPlot, layout);
  }).catch(error => {
    console.error('Error fetching data:', error);
  });
}

// Helper function to capitalize the first letter of each word
String.prototype.capitalize = function() {
  return this.replace(/(?:^|\s)\S/g, function(a) { return a.toUpperCase(); });
};

// Initialize the default plot with studio data
bedroomOptionChanged('studio');
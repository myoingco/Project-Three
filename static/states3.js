console.log("script");

// Function to handle the bedroom dropdown change event
function scatterplotchange(bedrooms) {
    console.log(bedrooms); // Check what value is being passed
  
    // Fetch data for the selected number of bedrooms
    d3.json(`/api/scatterplot?bedrooms=${bedrooms}`).then(function(data) {
      console.log(data); // Log the fetched data for debugging
  
      // Extract states and rent dollar changes from the data
      let population = data.map(d => d.population);
      let rentprice = data.map(d => d.rent_price);
      let countystate = data.map(d => d.county_state);

        // Define trace for Plotly scatter plot
        let trace = {
            x: population,
            y: rentprice,
            mode: 'markers',
            type: 'scatter',
            text: countystate, // Add county_state for hover information
            marker: {
                size: 12,
                opacity: 0.6,
                color: 'blue' // Adjust color as needed
            }
        };

        // Plotly data and layout
        let dataToPlot = [trace];
        let layout = {
            title: `Population vs. Rental Prices (${bedrooms.replace('_', ' ').capitalize()} Bedrooms)`,
            xaxis: { title: 'Population' },
            yaxis: { title: 'Rental Prices' }
        };

        // Plot the scatter plot
        Plotly.newPlot('scatterPlot', dataToPlot, layout);
    }).catch(error => {
        console.error('Error fetching data:', error);
    });
}

// Helper function to capitalize the first letter of each word
String.prototype.capitalize = function() {
    return this.replace(/(?:^|\s)\S/g, function(a) { return a.toUpperCase(); });
};

// Initialize the scatter plot with studio data
scatterplotchange('Studio');
// Initializes the page with a default plot
function init() {
    let data = [{
      x: [],
      y: []
    }];
    Plotly.newPlot("chart", data);
  }
  
  init();
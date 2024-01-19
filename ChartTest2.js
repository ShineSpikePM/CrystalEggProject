let airdata = d3.json('AirQuality.resources.json');
const ChartData =  fetch("https://raw.githubusercontent.com/LuzMaria04/Project-03-Team-Crystal-Egg/main/energydata.energypollution.json");
//console.log(airdata);


d3.json('AirQuality.resources.json').then(airdata => {
    // Specify the country you want to retrieve the values for
    let targetCity = 'Hotan'; // Replace with the desired city

    // Filter entries for the specified country
    const matchingEntries = airdata.filter(entry => entry.City === targetCity);
    let cities = [];
    let years = [];
    
  if (matchingEntries.length > 0) {
    for(var i = 0; i < matchingEntries.length; i++){
        cities.push(matchingEntries[i]["City"])
    }
  if (matchingEntries.length > 0){
        for(var i = 0; i < matchingEntries.length; i++){
            cities.push(matchingEntries[i]["Year"])
        }
    // Log the values for each instance of the country, including the new 'Year'
    /*matchingEntries.forEach(entry => {
      const valueForCity = entry.City;
      const valueForPollution = entry["Air Pollution"];
      const valueForYear = entry.Year;
      console.log(`City: ${valueForCity}, Year: ${valueForYear}, Air Pollution: ${valueForPollution}`);
    }); */
    console.log(cities);
    console.log(years);

  } else {
    console.log(`${targetCity} not found in the data.`);
  }
}}).catch(error => {
  console.error('Error loading JSON file:', error);

  const lineChart = document.getElementById('chart2');
  new Chart(lineChart, {
  // type of chart we want to create
  type: 'line',
  // the data for the chart
  data: {
  labels: labels,
  
  // add the data
  datasets: [{
      label: 'PM2.5 (Particles in air)',
      data: data,//[92,116,110,110,102],
      borderWidth: 1,
      backgroundColor: ['teal'],
      borderColor: 'black'
  }]
  },
  options: {
  scales: {
      y: {
      beginAtZero: true
      }
  }
  }
  
  });



});



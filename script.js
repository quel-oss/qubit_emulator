async function fetchText() { 
  //var url = "https://raw.githubusercontent.com/brandiqa/json-examples/master/src/db.json";
  //$.getJSON(url, function(json){
  //  document.getElementById('text2').innerHTML = json.clients[ 0 ].name;
  // });
  //document.getElementById('text2').innerHTML = "b";
}

  var canvas = document.getElementById('myChart');
  var canvas2 = document.getElementById('myChart2');
  
  var amp = [];
  var amp2 = [];
  var amp3 = [];
  var amp4 = [];

  for (var i = 0; i < 25; i++) {
    amp[i] = sampleData.samples[i].inputq0_I;
    amp2[i] = sampleData.samples[i].inputq0_Q;
    amp3[i] = sampleData.samples[i].inputq1_I;
    amp4[i] = sampleData.samples[i].inputq1_Q;
  }
  
  var data = {
    labels: Array.from(Array(25), (_, index) => 4*index),
    datasets: [{
      xAxisId: "xAxis",
      label: "I",
      fill: false,
      lineTension: 0.1,
      backgroundColor: "rgba(160,192,192,0.2)",
      borderColor: "rgba(192,72,192,1)",
      borderCapStyle: 'butt',
      borderDash: [],
      borderDashOffset: 0.0,
      borderJoinStyle: 'miter',
      pointBorderColor: "rgba(192,72,192,1)",
      pointBackgroundColor: "#fff",
      pointBorderWidth: 1,
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(192,72,192,1)",
      pointHoverBorderColor: "rgba(220,220,220,1)",
      pointHoverBorderWidth: 2,
      pointRadius: 2,
      pointHitRadius: 10,
      data: amp,
    },
    {
      label: "Q",
      fill: false,
      lineTension: 0.1,
      backgroundColor: "rgba(75,192,192,0.4)",
      borderColor: "rgba(75,192,192,1)",
      borderCapStyle: 'butt',
      borderDash: [],
      borderDashOffset: 0.0,
      borderJoinStyle: 'miter',
      pointBorderColor: "rgba(75,192,192,1)",
      pointBackgroundColor: "#fff",
      pointBorderWidth: 1,
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(75,192,192,1)",
      pointHoverBorderColor: "rgba(220,220,220,1)",
      pointHoverBorderWidth: 2,
      pointRadius: 5,
      pointHitRadius: 10,
      data: amp2,
    }
    ]
  };

  var data2 = {
    labels: Array.from(Array(25), (_, index) => 4*index),
    datasets: [{
      xAxisId: "xAxis",
      label: "I",
      fill: false,
      lineTension: 0.1,
      backgroundColor: "rgba(160,192,192,0.2)",
      borderColor: "rgba(192,72,192,1)",
      borderCapStyle: 'butt',
      borderDash: [],
      borderDashOffset: 0.0,
      borderJoinStyle: 'miter',
      pointBorderColor: "rgba(192,72,192,1)",
      pointBackgroundColor: "#fff",
      pointBorderWidth: 1,
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(192,72,192,1)",
      pointHoverBorderColor: "rgba(220,220,220,1)",
      pointHoverBorderWidth: 2,
      pointRadius: 2,
      pointHitRadius: 10,
      data: amp3,
    },
    {
      label: "Q",
      fill: false,
      lineTension: 0.1,
      backgroundColor: "rgba(75,192,192,0.4)",
      borderColor: "rgba(75,192,192,1)",
      borderCapStyle: 'butt',
      borderDash: [],
      borderDashOffset: 0.0,
      borderJoinStyle: 'miter',
      pointBorderColor: "rgba(75,192,192,1)",
      pointBackgroundColor: "#fff",
      pointBorderWidth: 1,
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(75,192,192,1)",
      pointHoverBorderColor: "rgba(220,220,220,1)",
      pointHoverBorderWidth: 2,
      pointRadius: 5,
      pointHitRadius: 10,
      data: amp4,
    }
    ]
  };

  var count = 96;

  function adddata() {
    if (count < 68*4){
      myLineChart.data.datasets[0].data[25] = sampleData.samples[count/4].inputq0_I;
      myLineChart.data.datasets[0].data.shift();
      myLineChart.data.datasets[1].data[25] = sampleData.samples[count/4].inputq0_Q;
      myLineChart.data.datasets[1].data.shift();
      myLineChart2.data.datasets[0].data[25] = sampleData.samples[count/4].inputq1_I;
      myLineChart2.data.datasets[0].data.shift();
      myLineChart2.data.datasets[1].data[25] = sampleData.samples[count/4].inputq1_Q;
      myLineChart2.data.datasets[1].data.shift();
    }
    // else{
    //   myLineChart.data.datasets[0].data[25] = Math.random() *2-1;
    //   myLineChart.data.datasets[0].data.shift();
    //   myLineChart.data.datasets[1].data[25] = Math.random() *2-1;
    //   myLineChart.data.datasets[1].data.shift();
    //   myLineChart2.data.datasets[0].data[25] = Math.random() *2-1;
    //   myLineChart2.data.datasets[0].data.shift();
    //   myLineChart2.data.datasets[1].data[25] = Math.random() *2-1;
    //   myLineChart2.data.datasets[1].data.shift();
    // }
    count += 4;
    myLineChart.data.labels[25] = count;
    myLineChart.data.labels.shift();
    myLineChart.update();
    myLineChart2.data.labels[25] = count;
    myLineChart2.data.labels.shift();
    myLineChart2.update();
    document.getElementById("text").innerHTML = count;
    document.getElementById("text2").innerHTML = sampleData.samples[10].time;
    fetchText();

  }

  function resetInterval(){
    clearInterval(intervalID);
    var intervalID = window.setInterval(adddata, 500);
  }
  
  var intervalId = window.setInterval(adddata, 500);
    
  const option =  {
      responsive: true,
      plugins:{
      title: {
        display: true,
        text: 'Input Control Qubit 0'
      },
      tooltips: {
        mode: 'label',
      }},
      hover: {
        mode: 'nearest',
        intersect: true
      }
    ,
      scales: {
        x: {
          title:{
            display: true,
            text: 'Time [ns]'
          }
        },
        y: {
          title:{
            display: true,
            text: 'Signal [amp]'
            }
          }
        }
      };

  const option2 =  {
      responsive: true,
      plugins:{
      title: {
        display: true,
        text: 'Input Control Qubit 1'
      },
      tooltips: {
        mode: 'label',
        }},
      hover: {
        mode: 'nearest',
        intersect: true
      },
      scales: {
        x: {
          title:{
            display: true,
            text: 'Time [ns]'
          }
        },
        y: {
          title:{
            display: true,
            text: 'Signal [amp]'
            }
          }
        }
      };
    
  var config = {
      type: 'line',
      data: data,
      options: option
    };

  var config2 = {
      type: 'line',
      data: data2,
      options: option2
    };
  
  var myLineChart = new Chart(
      canvas,
      config
  );

  var myLineChart2 = new Chart(
    canvas2,
    config2
);
  
  //var data = [data1,data2];
  

  
  var x = [];
  var y = [];
  
  x= [0,0,0,0,2,2,2,2,2];
  y= [2,0,0,0,0,0,2,2,2];
  /*
  for (var i = 0; i < 4; i++) {
    x[i] = Math.random();
    y[i] = Math.random() + 1;
  }*/
  /*
  var data = [{
    x: x,
    y: y,
    type: 'histogram2d',
      histnorm: 'probability',
      autobinx: false,
      xbins: {
        start: 0,
        end: 3,
        size: 1
      },
      autobiny: false,
      ybins: {
        start: 0,
        end: 3,
        size: 1
      }
  }];
  Plotly.newPlot('myDiv', data);
  */
  const ctx = document.getElementById('histogram').getContext('2d');
  const ctx2 = document.getElementById('histogram2').getContext('2d');
  
  var myBarChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['00', '01', '02','10','11','12','20','21','22'],
        datasets: [
          {
            data: [62,33,45,28,20,20,11,34,36],
            backgroundColor: ["rgba(91,39,219,0.5)","rgba(219,39,91,0.5)","rgba(39,219,91,0.5)","rgba(91,39,219,0.5)","rgba(219,39,91,0.5)","rgba(39,219,91,0.5)","rgba(91,39,219,0.5)","rgba(219,39,91,0.5)","rgba(39,219,91,0.5)"]
          }
        ]
      },
      options: {
        responsive: true,
        plugins:{
          title: {
            display: true,
            text: 'Each state Probability(X)'
          },
          legend:{
            display: false
          }
        },
        scales: {
          y: {
            suggestedMin: 50,
            suggestedMax: 100,
            ticks: {
              stepSize: 10,
              callback: function(value, index, values){
                return  (value*0.01).toFixed(2)
              }
            }
          }
        },
      }
    });

    var myBarChart = new Chart(ctx2, {
      type: 'bar',
      data: {
        labels: ['00', '01', '02','10','11','12','20','21','22'],
        datasets: [
          {
            data: [31,44,5,17,60,40,44,33,35],
            backgroundColor: ["rgba(91,39,219,0.5)","rgba(219,39,91,0.5)","rgba(39,219,91,0.5)","rgba(91,39,219,0.5)","rgba(219,39,91,0.5)","rgba(39,219,91,0.5)","rgba(91,39,219,0.5)","rgba(219,39,91,0.5)","rgba(39,219,91,0.5)"]
          }
        ]
      },
      options: {
        responsive: true,
        plugins:{
          title: {
            display: true,
            text: 'Each state ProbabilityZ)'
          },
          legend:{
            display: false
          }
        },
        scales: {
          y: {
            suggestedMin: 50,
            suggestedMax: 100,
            ticks: {
              stepSize: 10,
              callback: function(value, index, values){
                return  (value*0.01).toFixed(2)
              }
            }
          }
        },
      }
    });
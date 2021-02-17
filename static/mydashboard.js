anychart.onDocumentReady(function () {
    var data = [{'x': '(21.0, 28.0]',
'low': '22.62',
'q1': '81.65',
'median': '89.32',
'q3': '93.78',
'high': '99.7'},
{'x': '(28.0, 32.0]',
'low': '28.44',
'q1': '86.23',
'median': '92.1',
'q3': '95.5',
'high': '99.73'},
{'x': '(32.0, 36.0]',
'low': '27.1',
'q1': '88.02',
'median': '93.23',
'q3': '96.2',
'high': '99.67'},
{'x': '(36.0, 39.0]',
'low': '25.92',
'q1': '89.48',
'median': '94.04',
'q3': '96.6',
'high': '99.86'},
{'x': '(39.0, 43.0]',
'low': '28.87',
'q1': '90.58',
'median': '94.61',
'q3': '96.89',
'high': '99.8'},
{'x': '(43.0, 47.0]',
'low': '36.52',
'q1': '90.55',
'median': '94.59',
'q3': '96.84',
'high': '99.74'},
{'x': '(47.0, 52.0]',
'low': '30.22',
'q1': '91.14',
'median': '94.88',
'q3': '97.01',
'high': '99.81'},
{'x': '(52.0, 56.0]',
'low': '26.06',
'q1': '92.21',
'median': '95.5',
'q3': '97.35',
'high': '99.85'},
{'x': '(56.0, 61.0]',
'low': '48.39',
'q1': '93.19',
'median': '96.0',
'q3': '97.61',
'high': '99.83'},
{'x': '(61.0, 69.0]',
'low': '42.95',
'q1': '94.16',
'median': '96.54',
'q3': '97.87',
'high': '99.81'}];

    // create a chart
    chart = anychart.box();

    // create a box series and set the data
    series = chart.box(data);
    // set chart title
    chart.title("Box Plot: Probabilité");

    // set the titles of the axes
    chart.xAxis().title("Age");
   //chart.yAxis().title("Sales, $");

    // set the container id
    chart.container("container");

    // initiate drawing the chart
    chart.draw();

    });
    var data2 = [
      {
        x: ['giraffes', 'orangutans', 'monkeys'],
        y: [20, 14, 23],
        type: 'bar'
      }
    ];

    Plotly.newPlot('bar_chart', data2);

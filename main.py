import cgi
import sqlite3
import time

conn=sqlite3.connect('database.db')
c=conn.cursor()

c.execute("SELECT temperature, humidite, date FROM releves")
L = c.fetchall()


form = cgi.FieldStorage()
print("content-type: text/html; charset=iso-8859-1\n")

html = """
<!DOCTYPE HTML>
<html>
<head>  
  <script type="text/javascript">
  window.onload = function () {
    var chart = new CanvasJS.Chart("chartContainer",
    {
      title:{
        text: "Derniers Relevés"
      },

      axisX:{
        title: "Heure",
        gridThickness: 2,
        interval:1, 
        intervalType: "hour",        
        valueFormatString: "hh:mm TT", 
        labelAngle: -20
      },
      axisY: [{ 
        title : "Température",
        titleFontColor : "red"
        },
        {
        title : "Humidité",
        titleFontColor : "blue"
        }],
      data: [
      {        
        type: "line",
        dataPoints: [//array
        {x: Date(Date.UTC (2012, 01, 1, 1,0) ), y: 26 },
        {x: new Date( Date.UTC (2012, 01, 1,2,0) ), y: 38  },
        {x: new Date( Date.UTC(2012, 01, 1,3,0) ), y: 43 },
        {x: new Date( Date.UTC(2012, 01, 1,4,0) ), y: 29},
        {x: new Date( Date.UTC(2012, 01, 1,5,0) ), y: 41},
        {x: new Date( Date.UTC(2012, 01, 1,6,0) ), y: 54},
        {x: new Date( Date.UTC(2012, 01, 1,7,0) ), y: 66},
        {x: new Date( Date.UTC(2012, 01, 1,8,0) ), y: 60},
        {x: new Date( Date.UTC(2012, 01, 1,9,0) ), y: 53},
        {x: new Date( Date.UTC(2012, 01, 1,10,0) ), y: 60}
        ]
      },
      {        
        type: "line",
        dataPoints: [//array
        {x: Date(Date.UTC (2012, 01, 1, 1,0) ), y: 5 },
        {x: new Date( Date.UTC (2012, 01, 1,2,0) ), y: 24  },
        {x: new Date( Date.UTC(2012, 01, 1,3,0) ), y: 46 },
        {x: new Date( Date.UTC(2012, 01, 1,4,0) ), y: 56},
        {x: new Date( Date.UTC(2012, 01, 1,5,0) ), y: 2},
        {x: new Date( Date.UTC(2012, 01, 1,6,0) ), y: 54},
        {x: new Date( Date.UTC(2012, 01, 1,7,0) ), y: 66},
        {x: new Date( Date.UTC(2012, 01, 1,8,0) ), y: 60},
        {x: new Date( Date.UTC(2012, 01, 1,9,0) ), y: 53},
        {x: new Date( Date.UTC(2012, 01, 1,10,0) ), y: 60}
        ]
      }
      ]
    });

chart.render();
}
</script>
<script type="text/javascript" src="https://canvasjs.com/assets/script/canvasjs.min.js"></script>
</head>
<body>
  <div id="chartContainer" style="height: 300px; width: 100%;">
  </div>
</body>
</html>
"""

print(html)

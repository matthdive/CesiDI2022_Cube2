import cgi
import sqlite3
import time
import random

conn=sqlite3.connect('database.db')
c=conn.cursor()

c.execute("SELECT temperature, humidite, date FROM (SELECT id_releve, temperature, humidite, date FROM releves ORDER BY id_releve DESC LIMIT 10) ORDER BY id_releve")
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
        valueFormatString: "HH:mm", 
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
        {x: new Date(""" + f"{str(L[0][2][6:10])}, {str(L[0][2][3:5])}, {str(L[0][2][0:2])}, {str(L[0][2][11:13])}, {str(L[0][2][14:16])},0" + """), y: """ + str(L[0][1]) + """},
        {x: new Date(""" + f"{str(L[1][2][6:10])}, {str(L[1][2][3:5])}, {str(L[1][2][0:2])}, {str(L[1][2][11:13])}, {str(L[1][2][14:16])},0" + """), y: """ + str(L[1][1]) + """},
        {x: new Date(""" + f"{str(L[2][2][6:10])}, {str(L[2][2][3:5])}, {str(L[2][2][0:2])}, {str(L[2][2][11:13])}, {str(L[2][2][14:16])},0" + """), y: """ + str(L[2][1]) + """},
        {x: new Date(""" + f"{str(L[3][2][6:10])}, {str(L[3][2][3:5])}, {str(L[3][2][0:2])}, {str(L[3][2][11:13])}, {str(L[3][2][14:16])},0" + """), y: """ + str(L[3][1]) + """},
        {x: new Date(""" + f"{str(L[4][2][6:10])}, {str(L[4][2][3:5])}, {str(L[4][2][0:2])}, {str(L[4][2][11:13])}, {str(L[4][2][14:16])},0" + """), y: """ + str(L[4][1]) + """},
        {x: new Date(""" + f"{str(L[5][2][6:10])}, {str(L[5][2][3:5])}, {str(L[5][2][0:2])}, {str(L[5][2][11:13])}, {str(L[5][2][14:16])},0" + """), y: """ + str(L[5][1]) + """},
        {x: new Date(""" + f"{str(L[6][2][6:10])}, {str(L[6][2][3:5])}, {str(L[6][2][0:2])}, {str(L[6][2][11:13])}, {str(L[6][2][14:16])},0" + """), y: """ + str(L[6][1]) + """},
        {x: new Date(""" + f"{str(L[7][2][6:10])}, {str(L[7][2][3:5])}, {str(L[7][2][0:2])}, {str(L[7][2][11:13])}, {str(L[7][2][14:16])},0" + """), y: """ + str(L[7][1]) + """},
        {x: new Date(""" + f"{str(L[8][2][6:10])}, {str(L[8][2][3:5])}, {str(L[8][2][0:2])}, {str(L[8][2][11:13])}, {str(L[8][2][14:16])},0" + """), y: """ + str(L[8][1]) + """},
        {x: new Date(""" + f"{str(L[9][2][6:10])}, {str(L[9][2][3:5])}, {str(L[9][2][0:2])}, {str(L[9][2][11:13])}, {str(L[9][2][14:16])},0" + """), y: """ + str(L[9][1]) + """}
        ]
      },
      {        
        type: "line",
        dataPoints: [//array
        {x: new Date(""" + f"{str(L[0][2][6:10])}, {str(L[0][2][3:5])}, {str(L[0][2][0:2])}, {str(L[0][2][11:13])}, {str(L[0][2][14:16])},0" + """), y: """ + str(L[0][0]) + """},
        {x: new Date(""" + f"{str(L[1][2][6:10])}, {str(L[1][2][3:5])}, {str(L[1][2][0:2])}, {str(L[1][2][11:13])}, {str(L[1][2][14:16])},0" + """), y: """ + str(L[1][0]) + """},
        {x: new Date(""" + f"{str(L[2][2][6:10])}, {str(L[2][2][3:5])}, {str(L[2][2][0:2])}, {str(L[2][2][11:13])}, {str(L[2][2][14:16])},0" + """), y: """ + str(L[2][0]) + """},
        {x: new Date(""" + f"{str(L[3][2][6:10])}, {str(L[3][2][3:5])}, {str(L[3][2][0:2])}, {str(L[3][2][11:13])}, {str(L[3][2][14:16])},0" + """), y: """ + str(L[3][0]) + """},
        {x: new Date(""" + f"{str(L[4][2][6:10])}, {str(L[4][2][3:5])}, {str(L[4][2][0:2])}, {str(L[4][2][11:13])}, {str(L[4][2][14:16])},0" + """), y: """ + str(L[4][0]) + """},
        {x: new Date(""" + f"{str(L[5][2][6:10])}, {str(L[5][2][3:5])}, {str(L[5][2][0:2])}, {str(L[5][2][11:13])}, {str(L[5][2][14:16])},0" + """), y: """ + str(L[5][0]) + """},
        {x: new Date(""" + f"{str(L[6][2][6:10])}, {str(L[6][2][3:5])}, {str(L[6][2][0:2])}, {str(L[6][2][11:13])}, {str(L[6][2][14:16])},0" + """), y: """ + str(L[6][0]) + """},
        {x: new Date(""" + f"{str(L[7][2][6:10])}, {str(L[7][2][3:5])}, {str(L[7][2][0:2])}, {str(L[7][2][11:13])}, {str(L[7][2][14:16])},0" + """), y: """ + str(L[7][0]) + """},
        {x: new Date(""" + f"{str(L[8][2][6:10])}, {str(L[8][2][3:5])}, {str(L[8][2][0:2])}, {str(L[8][2][11:13])}, {str(L[8][2][14:16])},0" + """), y: """ + str(L[8][0]) + """},
        {x: new Date(""" + f"{str(L[9][2][6:10])}, {str(L[9][2][3:5])}, {str(L[9][2][0:2])}, {str(L[9][2][11:13])}, {str(L[9][2][14:16])},0" + """), y: """ + str(L[9][0]) + """}
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

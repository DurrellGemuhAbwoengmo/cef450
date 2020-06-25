import cherrypy
import pandas as pd
import numpy as np
import string
import os
import os.path
import myprocessor

p = myprocessor.MyProcessor()


class app(object):
    @cherrypy.expose
    
    def index(self):
        data = {"num1": [1, 2, 3, 42, 5, 5, 15, 1, 25, 68, 100] }
        df = pd.DataFrame(data)
        a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
        output = p.run(df)
        return """
    <!DOCTYPE html>
<html>

<head>
    <title>CEF450: Project</title>
    <!-- <link rel="stylesheet" type="text/css" href="stylesheet.css"> -->
    <style type="text/css" >
        
            body{
                background: #D3D7CF;
            }
            .navbar{font-weight: bold;}
            .navbar:hover{color: #151814; background-color: #DFFFD6; text-transform: uppercase; font-weight: normal;}
            .a:active{background-color:red;}
            .header{text-align: center; color: blue;}
            .foot{display: flex; text-align: right;}
        </style>
</head>

<body>
    <nav class="navbar">
        <ul>
        <li><a href="#">Home</a></li>
        <li><a href="#About">About Group</a></li>
        <li><a href="#">Solution</a></li>
        <li><a href="#">Contact</a></li>
        </ul>
        </nav>
	<div class="header">
		<h1>FACULTY OF ENGINEERING AND TECHNOLOGY</h1>
		<h2>DEPARTMENT OF COMPUTER ENGINEERING</h2>
        <h3>CEF450-CLOUD COMPUTING AND SERVICE ORIENTED ARCHITECTURE</h3>
        <h4>Lecture: Mr. SOP DEFFO Lionel Landry</h4>
	</div>
	<hr>
	<h2 class="project">CEF450 Project: Project Specification and Proposed Work Flow</h2>
	<p>This Project will count as part of as our continuous assessment for the course CEF450 as explained by
		the Course instructor, and its due this week.</p>
	<p>The project specification goes thus:</p>
	<ul>
		<li>Create a web service a to take a series of numbers and displaying its maximum and minimum.</li>
		<li>Create a web service able to take two statistical distributions (of at least 10 elements) and
			returning the variance, standard deviation, covariance matrix and correlation coefficient of both.</li>
	</ul>
    <h4><strong>NB: Producing a user interface is a bonus.</strong></h4>
    <hr>
	<br>
	<h3><u>PROPOSED WORKFLOW</u></h3>
	<p>To ensure thing work properly and to track participation, here is a proposed workflow. Amendments to
		this workflow are welcome.</p>
	<ul>
		<li>Analysis of the Project.</li>
		<li>Proposition of interface and algorithms</li>
		<li>Implementation</li>
		<li>Report writing</li>
	</ul>
	<h3><strong>NB: Participation is compulsory, else the defaulter won’t find his/her name on the project
			report.</strong></h3>
	<h3><strong>Thanks!!</strong></h3>
    <hr>
    <div class="About">
        <h1>About the group</h1>
    <h4>Group Leader: </h4>
    <h4>Number of participants: six(06)</h3>
    <h4>Group members</h4>
    <table border="1" class="dataframe">
        <thead>
          <tr style="text-align: center;">
           <th>Number</th>
            <th>Name</th>
            <th>Matricule</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>1</td>
            <td>Ashu Reiziger Achuo</td>
            <td>FE17A002</td>
          </tr>
          <tr>
            <td>2</td>
            <td>Bassah Roselyn Nahjela</td>
            <td>FE17A009</td>
          </tr>
          <tr>
            <td>3</td>
            <td>Durrell Gemuh Abwoengmo</td>
            <td>FE17A019</td>
          </tr>
          <tr>
            <td>4</td>
            <td>Mafany Tande Myles</td>
            <td>FE17A037</td>
          </tr>
          <tr>
            <td>5</td>
            <td>Mobou Defo Yolande</td>
            <td>FE17A043</td>
          </tr>
          <tr>
            <td>6</td>
            <td>Ndimbu Courage Mah</td>
            <td>FE17A049</td>
          </tr>
         
        </tbody>
      </table>
      <h4>Task allocation to amongst group members</h4>
      <table border="1" class="dataframe">
        <thead>
          <tr style="text-align: center;">
            <th>Name</th>
            <th>Task</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Ashu Reiziger Achuo</td>
            <td>Report writing</td>
          </tr>
          <tr>
            <td>Bassah Roselyn Nahjela</td>
            <td>Interface design</td>
          </tr>
          <tr>
            <td>Durrell Gemuh Abwoengmo</td>
            <td>Implementation</td>
          </tr>
          <tr>
            <td>Mafany Tande Myles</td>
            <td>Proposition of algorithms</td>
          </tr>
          <tr>
            <td>Mobou Defo Yolande</td>
            <td>Interface design</td>
          </tr>
          <tr>
            <td>Ndimbu Courage Mah</td>
            <td>Analysis of project</td>
          </tr>
         
        </tbody>
      </table>
    </div>
    <hr>
	<h2>Tasks</h2>
	<ol>
		<li>Create a web service a to take a series of numbers and displaying its maximum and minimum.</li> 
		<a href="./index.html" ><button type="button" >Solution</button> </a><br>

        <br>
		<li>Create a web service able to take two statistical distributions (of at least 10 elements) and
			returning the variance, standard deviation, covariance matrix and correlation coefficient of both.</li>
		<a href="../question2.html" ><button type="button" >Solution</button> </a>
    </ol>
    <hr>
  
</body>

</html>

    """, """Solution to question 1""",output.to_html(), """Solution to question 2""",str(np.var(a)), """<!DOCTYPE html>
<html>
	<head>
		<title>Question 1</title>
	</head>
	<body>
		<div class="foot"><h6>Copy right</h6> <h6>&copy;</h6> <h6>property of Durrell Gemuh</h6></div>
	</body>
</html>"""

    # @cherrypy.expose
    # def second(self):
    #     a = np.array([[1, 2, 3, 4] dtype=np.int64)
    #     return str(np.var(a))


if __name__ == '__main__':
    cherrypy.quickstart(app())

import cherrypy
import pandas as pd
import myprocessor

p = myprocessor.MyProcessor()

class app(object):
    @cherrypy.expose
    def index(self):
        
        data = {"num1" : [1, 2, 3], "num2":[4, 5, 6]}
        df = pd.DataFrame(data)
        output = p.run(df)
        return output.to_html()
    
    

if __name__ == '__main__':
    cherrypy.quickstart(app())
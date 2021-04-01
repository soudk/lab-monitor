# lab-monitor
Basic software to display temperatures, pressures and other environmental variables from a slow control system on a web app.  

Uses: Flask, Bootstrap, Highcharts.

Based on [Flask Charts Youtube Tutorials

 by soumilshah1995](https://github.com/soumilshah1995/Flask-Charts-Youtube-Tutorials-)

## Usage

- In `app.py` change the variable `my\_csv\_file` to your live-populated csv file. 
- execute by `python app.py` 
- Open your browser to [http://localhost:5000](http://localhost:5000) and view your data


### Demo

You can demo the program by running `python dummy_csv_writer/write_dummy_csv.py` in a separate terminal window. This will continuously populate a csv with random data for testing. 

You can then use the program following the usage instruction and it will use the dummy csv file to generate the graphs.

Remember to stop running `write\_dummy\_csv.py` when you are done!



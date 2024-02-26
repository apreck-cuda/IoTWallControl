from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    in1read = subprocess.run(["cat /sys/class/gpio/gpio106/value"], capture_output=True, shell=True, text=True)
    in1bool = int(in1read.stdout.strip())
    in2read = subprocess.run(["cat /sys/class/gpio/gpio107/value"], capture_output=True, shell=True, text=True)
    in2bool = int(in2read.stdout.strip())
    in3read = subprocess.run(["cat /sys/class/gpio/gpio108/value"], capture_output=True, shell=True, text=True)
    in3bool = int(in3read.stdout.strip())
    in4read = subprocess.run(["cat /sys/class/gpio/gpio109/value"], capture_output=True, shell=True, text=True)
    in4bool = int(in4read.stdout.strip())
    return render_template('index.html', in1bool=in1bool, in2bool=in2bool, in3bool=in3bool, in4bool=in4bool)


#####Output API#########
@app.route('/out1/<int:state>',methods = ['POST'])
def control_out1(state):
    if state == 0:
        print("Out 1 OFF")
        subprocess.run(["echo 0 > /sys/class/gpio/gpio110/value"], capture_output=True, shell=True)
        #return render_template("index.html")
    elif state == 1:
        print("Out 1 ON")
        subprocess.run(["echo 1 > /sys/class/gpio/gpio110/value"], capture_output=True, shell=True)
    return 'OK'

@app.route('/out2/<int:state>',methods = ['POST'])
def control_out2(state):
    if state == 0:
        print("Out 2 OFF")
        subprocess.run(["echo 0 > /sys/class/gpio/gpio111/value"], capture_output=True, shell=True)
        #return render_template("index.html")
    elif state == 1:
        print("Out 2 ON")
        subprocess.run(["echo 1 > /sys/class/gpio/gpio111/value"], capture_output=True, shell=True)
    return 'OK'

@app.route('/out3/<int:state>',methods = ['POST'])
def control_out3(state):
    if state == 0:
        print("Out3 OFF")
        subprocess.run(["echo 0 > /sys/class/gpio/gpio112/value"], capture_output=True, shell=True)
        #return render_template("index.html")
    elif state == 1:
        print("Out 3 ON")
        subprocess.run(["echo 1 > /sys/class/gpio/gpio112/value"], capture_output=True, shell=True)
    return 'OK'

@app.route('/out4/<int:state>',methods = ['POST'])
def control_out4(state):
    if state == 0:
        print("Out 4 OFF")
        subprocess.run(["echo 0 > /sys/class/gpio/gpio113/value"], capture_output=True, shell=True)
        #return render_template("index.html")
    elif state == 1:
        print("Out 4 ON")
        subprocess.run(["echo 1 > /sys/class/gpio/gpio113/value"], capture_output=True, shell=True)
    return 'OK'
#################Input API##############

@app.route('/in1')
def state_in1():
    instate = subprocess.run(["cat /sys/class/gpio/gpio106/value"], capture_output=True, shell=True, text=True)

    if instate.returncode == 0:
        checkbox_state = int(instate.stdout.strip())
        in1_state = {
            "state": checkbox_state,
            "IN ID": 1
        }
        return jsonify(in1_state), 200
    else:
        error_message = {
            "error": "Exec failed",
            "IN ID": 1
        }
        return jsonify(error_message), 500

@app.route('/in2')
def state_in2():
    instate = subprocess.run(["cat /sys/class/gpio/gpio107/value"], capture_output=True, shell=True, text=True)

    if instate.returncode == 0:
        checkbox_state = int(instate.stdout.strip())
        in1_state = {
            "state": checkbox_state,
            "IN ID": 2
        }
        return jsonify(in1_state), 200
    else:
        error_message = {
            "error": "Exec failed",
            "IN ID": 2
        }
        return jsonify(error_message), 500   
    
@app.route('/in3')
def state_in3():
    instate = subprocess.run(["cat /sys/class/gpio/gpio108/value"], capture_output=True, shell=True, text=True)

    if instate.returncode == 0:
        checkbox_state = int(instate.stdout.strip())
        in1_state = {
            "state": checkbox_state,
            "IN ID": 3
        }
        return jsonify(in1_state), 200
    else:
        error_message = {
            "error": "Exec failed",
            "IN ID": 3
        }
        return jsonify(error_message), 500  

@app.route('/in4')
def state_in4():
    instate = subprocess.run(["cat /sys/class/gpio/gpio109/value"], capture_output=True, shell=True, text=True)

    if instate.returncode == 0:
        checkbox_state = int(instate.stdout.strip())
        in1_state = {
            "state": checkbox_state,
            "IN ID": 4
        }
        return jsonify(in1_state), 200
    else:
        error_message = {
            "error": "Exec failed",
            "IN ID": 4
        }
        return jsonify(error_message), 500  

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3333)
from flask import Flask,send_file,request
import requests,json,datetime

app = Flask(__name__)



@app.route('/about')
def about():
    receiver_id=request.args.get('id')
    filename = "pixel.png"
    log_file_path="images/spy_pixel_logs.txt"

    current_time = datetime.datetime.now()
    timestamp = datetime.datetime.strftime(current_time, "%Y-%m-%d %H:%M:%S")

    client_ip =  request.remote_addr
    url = f'https://api.ipbase.com/v2/info?apikey=ipb_live_aDj4XlcobaLxlUSDAdItoccKXaEKXM33vHYKIcTZ&ip={client_ip}'
   
    print('------')
    print(client_ip)
    print(timestamp)
    print(receiver_id)
    print('------')

    response = requests.get(url)
    data_dict = response.json()
    data_dict['timestamp'] = timestamp


    data_dict['id_of_email_reciever'] =id
    with open(log_file_path, 'a') as file:
        json.dump(data_dict, file, indent=4)
        file.write('\n')


    return send_file(filename, mimetype="image/png")


if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0', port=8000)


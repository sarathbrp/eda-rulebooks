from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        # Here you will get the JSON payload sent by the webhook
        payload = request.json

        # you can print the payload
        print("Received Payload:", payload)

        # You can send a response if required
        response = {"message": "Webhook received successfully"}
        return jsonify(response), 200
    except Exception as e:
        return str(e), 400

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000

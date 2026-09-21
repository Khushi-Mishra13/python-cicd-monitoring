from flask import Flask
from prometheus-client import counter, gernerate_latest

app = Flask(__name__)

REQUEST_COUNT = Counter(
	"app_requests_total",
	"Total number of  requests")

@app.route("/")
def home() :
	return "CICD app is running"

@app.route("/health")
def health() :
	return "OK", 200

@app.route("/metrics")
def metrics() :
	return generate_latest(), 200, {
		"Content-Type": "text/plain; version=0.04"
	}
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8083)


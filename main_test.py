import requests

from .main import wait_for_connect, create_kafka_connector


def test_wait_for_connect():
    kafka_connect_url = "connect:8083"
    timeout = 60

    # this will exit(1) if connection is not successful
    wait_for_connect()

    # test if kafka connect is up
    r = requests.get("http://" + kafka_connect_url)
    assert r.status_code == 200

def test_create_kafka_connector():
    connect_url = "connect:8083"
    connector_name = "test_file_sink"
    connector_config = {
      "name": connector_name,
      "connector.class": "org.apache.kafka.connect.file.FileStreamSinkConnector",
      "topics": "test_topic",
      "tasks.max": "1"
    } 

    create_kafka_connector(connector_config)

    # validate connector creation
    r = requests.get("http://" + connect_url + "/connectors/" + connector_name)
    assert r.status_code == 200
    

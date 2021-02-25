import json
import os
import logging
import time
import requests

from config import configs

def wait_for_connect():
    connect_url = configs.KAFKA_CONNECT_URL
    max_retries = configs.KAFKA_CONNECT_INIT_TIMEOUT

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    retry_count = 0
    while True:
        if retry_count >= max_retries:
            # if connect is still not up in 2 minutes, give up
            logger.error("Kafka connect unreachable, failed to create sinks")
            exit(1)
        try:
            r = requests.get("http://" + connect_url)
            if r.status_code == 200:
                break
            else:
                retry_count += 1
                logger.info(
                    "Could not connect to kafka-connect, retrying in 1 sec: "
                    + str(retry_count)
                    + " retries"
                )
                time.sleep(1)
        except:
            retry_count += 1
            logger.info(
                "Could not connect to kafka-connect, retrying in 1 sec: "
                + str(retry_count)
                + " retries"
            )
            time.sleep(1)

    # kafka connect is up
    logger.info("Creating kafka connectors...")

def create_kafka_connector(connector_config):
    connect_url = configs.KAFKA_CONNECT_URL

    url = "http://" + connect_url + "/connectors"
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    data = json.dumps(connector_config)

    r = requests.post(url, headers=headers, data=data)


def main():
    connector_configs_path = configs.KAFKA_CONNECT_INIT_CONNECTORS_PATH
    connector_configs = os.listdir(connector_configs_path)

    # wait for connect to start it's rest-api
    wait_for_connect()

    for p in connector_configs:
        with open(os.path.join(connector_configs_path, p)) as f:
            c = json.load(f)
        create_kafka_connector(c)
        print("Created connector: " + c["name"])


if __name__ == '__main__':
    main()

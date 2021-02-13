# kafka-connect-init

Init container to be used with [icon-api]() stack. 
Use this contianer to set up kafka connectors.

Docker Hub: [image](http://hub.docker.com/r/pranavt61/icon-kafka-connect-init)

## Edit the connector-name.json in the configs dir
```
{
  "name": "event-registration-posgtres-sink",
  "config": {
    "connector.class": "io.confluent.connect.jdbc.JdbcSinkConnector",
    "topics": "event_registrations",
    "tasks.max": "1",
    "connection.url": "jdbc:postgresql://postgres:5432/postgres",
    "connection.password": "changethis",
    "value.converter.schema.registry.url": "http://schemaregistry:8081",
    "key.converter.schemas.enable": "false",
    "delete.enabled": "true",
    "auto.evolve": "true",
    "connection.user": "admin",
    "value.converter.schemas.enable": "true",
    "auto.create": "true",
    "value.converter": "io.confluent.connect.json.JsonSchemaConverter",
    "key.converter": "org.apache.kafka.connect.storage.StringConverter",
    "pk.mode": "record_key",
    "pk.fields": "reg_id",
    "insert.mode": "upsert"
  }
}
```

## Docker Build
```
docker build . -t icon-kafka-connect-init:latest
docker run \
  -e KAFKA_CONNECT_URL="connect:8083" \
  icon-kafka-connect-init:latest
```

## Docker Compose set up
```
  kafka-connect-init:
    image: pranavt61/icon-kafka-connect-init:latest
    depends_on:
      - connect
    env_file:
      - .env
    restart: on-failure

```

## Enviroment Variables

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| KAFKA_CONNECT_URL | location of kafka connect | NULL | True |
| KAFKA_CONNECT_INIT_TIMEOUT | how many seconds to wait for kafka connect to come up | 120 | FALSE |

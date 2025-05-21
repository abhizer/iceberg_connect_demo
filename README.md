# Feldera Iceberg Kafka Connect Demo

This demonstration will send data from Feldera to an Apache Kafka topic which will be picked up by the Iceberg Connector for Kafka Connect and written to an Iceberg table.

## Technologies involved
- Feldera
- Apache Kafka
- Kafka Connect
- Apache Iceberg
- MinIo
- Python

## Steps to run demo
1. Launch server applications

    `docker compose up -d`

2. Create Kafka topic

    `docker exec -t broker kafka-topics --create --topic completed-pizzas --partitions 6 --bootstrap-server broker:9092`

3. Launch the Iceberg connector (installed via docker compose)

    `curl -X PUT http://localhost:8083/connectors/pizzas-on-ice/config \
     -i -H "Content-Type: application/json" -d @pizzas_on_ice.json`

4. Check status of connector

    `curl http://localhost:8083/connectors/pizzas-on-ice/status |jq`

5. Install `feldera` package

    `pip install feldera`

6. Start the Feldera pipeline.

    `python start_feldera_pipeline.py`

7. Clean up resources when you're done.

    `docker compose down`

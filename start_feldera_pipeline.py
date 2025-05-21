from feldera import PipelineBuilder, FelderaClient

name = "feldera-kafka-iceberg-demo"
sql = """
create table tbl (
    order_number int,
    pizza_name varchar,
    quantity int,
    toppings varchar array
) with (
    'connectors' = '[{
        "transport": {
            "name": "datagen",
            "config": {
                "plan": [{
                    "limit": 100,
                    "rate": 1
                }]
            }
        }
    }]'
);

create materialized view pizzas with (
   'connectors' = '[
    {
      "transport": {
          "name": "kafka_output",
          "config": {
              "bootstrap.servers": "broker:9092",
              "topic": "completed-pizzas"
          }
      },
      "format": {
          "name": "json",
          "config": {
              "update_format": "insert_delete",
              "array": false
          }
      }
   }
   ]'
) as select * from tbl order by order_number desc limit 10;
"""
pipeline = PipelineBuilder(FelderaClient.localhost(), name, sql).create_or_replace()
pipeline.start()

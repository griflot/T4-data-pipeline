# 5G-data-pipeline
Start Kafka broker:\
`docker compose up`

Enter data manually:\
`python /scripts/kafka-prodcuer.py`

View data within broker container (temporary):\
```
docker exec --workdir /opt/kafka/bin --it kafka-broker sh
./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic student-grades --from-beginning
```
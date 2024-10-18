# T4-data-pipeline
## Start pipeline services
Start Mage and Kafka broker from terminal: `docker compose up`

To access Mage's UI, navigate to `localhost:6789` on your web browser.

## Create pipelines
Creating a Pipeline:
1. Select "Pipelines" from the left menu bar
2. Select "+ New"
3. Select "Standard (batch)" for pipelining batch data or "Streaming" for pipelining event streaming data
4. Once the you name and create the pipeline: data loader, data transformer, and data exporter blocks can be created within the "Edit pipeline" tab
5. To test the pipeline's execution, press the green "Execute pipeline" button on the right side of the "Edit pipeline" tab

## End pipeline services
Stop Mage and Kafka broker from terminal: `docker compose down`

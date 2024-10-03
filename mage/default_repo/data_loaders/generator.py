from mage_ai.streaming.sources.base_python import BasePythonSource
from typing import Callable
import json

if 'streaming_source' not in globals():
    from mage_ai.data_preparation.decorators import streaming_source


@streaming_source
class CustomSource(BasePythonSource):
    def init_client(self):
        """
        Implement the logic of initializing the client.
        """

    def batch_read(self, handler: Callable):
        """
        Batch read the messages from the source and use handler to process the messages.
        """
        test_records = [{
            "name": "Stacy",
            "grade": "A"
        }, {
            "name": "Bob",
            "grade": "F"
        }, {
            "name": "Ly",
            "grade": "F-"
        }, {
            "name": "Griffin",
            "grade": "A+"
        }]
        records_processed = False
        while True:
            records = []
            # Implement the logic of fetching the records
            if not records_processed:
                for item in test_records:
                    records.append(json.dumps(item))
                records_processed = True
            if len(records) > 0:
                handler(records)

"""Streamlit Connection for Notion API."""
import os
from streamlit.connections import BaseConnection
from streamlit.runtime.caching import cache_data
from notion_client import Client

import pandas as pd

class NotionConnection(BaseConnection[Client]):
    """A Streamlit Connection for Notion API."""
    def _connect(self, **kwargs) -> Client:
        if "notion_api_key" in kwargs:
            api_key = kwargs.pop("notion_api_key")
        elif "notion_api_key" in self._secrets:
            api_key = self._secrets["notion_api_key"]
        else:
            api_key = os.environ.get("NOTION_API_KEY")
            if api_key is None:
                raise ValueError("Notion API key not found.")
        client = Client(auth=api_key)

        return client

    def list_databases(self):
        """List all databases."""
        return self._instance.search(filter={"value":"database", "property": "object"})

    def api(self):
        """Return the Notion API client."""
        return self._instance

    def query(
        self, database_id, ttl: int = 3600, **kwargs
    ) -> dict:
        """Query a database."""
        @cache_data(ttl=ttl)
        def _query(database_id: str = None, **kwargs) -> pd.DataFrame:
            return self._instance.databases.query(
                database_id=database_id, **kwargs
            )["results"]

        return _query(database_id=database_id, **kwargs)

# 🔗 Streamlit Notion Connection: Unlock the Power of Notion in Your Data Apps

**Effortlessly integrate Notion Connection with your Streamlit apps to enhance data interaction and visualization**

## Why Streamlit Notion Connection?

As more teams and individuals rely on Notion for project management, note-taking, and collaboration, the ability to seamlessly connect Notion with your data applications becomes invaluable. Streamlit Notion API allows you to effortlessly integrate Notion's powerful API into your Streamlit apps, enabling you to fetch, manipulate, and visualize data from Notion databases and pages. This integration empowers your Streamlit data apps to leverage the rich data stored in Notion, creating more dynamic and interactive user experiences.

## Installation

`pip install st-notion-connection`

## Usage
### Obtaining Notion API Credentials

To use the Notion API, you need to obtain an API key by creating an integration in the Notion Developer Portal. Follow these steps:

1. **Go to the Notion Developer Portal:**
   Visit [Notion Developer Portal](https://www.notion.so/my-integrations).

2. **Create a New Integration:**
   - Click on the "New integration" button.
   - Fill in the required details such as name, and select the workspace you want to integrate with.
   - Set the integration type to "Internal Integration".

3. **Save the Integration:**
   - Once the integration is created, you will be provided with an "Internal Integration Token". Copy this token.

4. **Add the Integration to Your Workspace:**
   - Go to the workspace you selected during integration creation.
   - Click on "Share" in the top-right corner.
   - Add the integration you created to the workspace.

### Setting Up the Notion API Key

You can provide the Notion API key in three ways:
1. As a parameter when creating an instance of `NotionConnection`.
2. As a secret in Streamlit's secrets management.
3. As an environment variable `NOTION_API_KEY`.

## Examples
```python
import streamlit as st
from streamlit_notion import NotionConnection

# Create connection
conn = st.connection("notion", type=NotionConnection)

databases = conn.list_databases()

# st.write(databases)

for database in databases["results"]:
    r = conn.query(database["id"], page_size=1)
    st.write(r)
```

### Methods

- `list_databases()`: Lists all databases in the Notion workspace.
- `api()`: Returns the Notion client instance.
- `query(database_id, ttl=3600, **kwargs)`: Queries a Notion database and caches the results for a specified time-to-live (TTL).

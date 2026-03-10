import gradio as gr
import sqlite3
import pandas as pd
import os

DB_PATH = "compdb.db"

def get_roster_details(row_limit: int = 100):
    """
    Fetches the roster_details table from the compdb.db database.
    
    Args:
        row_limit: The maximum number of rows to return (default is 100).
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        # We fetch only a limited number of rows by default to avoid large payloads
        query = f"SELECT * FROM roster_details LIMIT {row_limit}"
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df
    except Exception as e:
        return f"Error: {str(e)}"

# Create Gradio interface
with gr.Blocks(title="Company Roster Explorer") as demo:
    gr.Markdown("# 🏢 Company Roster Explorer")
    gr.Markdown("This application exposes the `roster_details` table from `compdb.db` also available as an MCP tool.")
    
    with gr.Row():
        limit_input = gr.Number(value=100, label="Row Limit", precision=0)
        fetch_btn = gr.Button("Fetch Roster Data", variant="primary")
    
    output_table = gr.Dataframe(label="Roster Details")
    
    fetch_btn.click(
        fn=get_roster_details,
        inputs=[limit_input],
        outputs=[output_table]
    )

if __name__ == "__main__":
    # Launching with mcp_server=True exposes the get_roster_details function as an MCP tool
    print("Launching Gradio app with MCP server enabled...")
    demo.launch(mcp_server=True, port=7860)

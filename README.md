# Gradio DB Explorer 🏢

A simple Gradio web application to explore the `roster_details` table from `compdb.db`. This application also exposes its core functionality as an **MCP (Model Context Protocol)** tool.

## 🚀 Setting Up the Environment

### 1. Create a Virtual Environment (if not already created)
```powershell
python -m venv venv
```

### 2. Activate the Virtual Environment
Run the command corresponding to your terminal:

**PowerShell:**
```powershell
.\venv\Scripts\Activate.ps1
```

**Command Prompt (cmd):**
```cmd
.\venv\Scripts\activate.bat
```

**Git Bash / Unix-like:**
```bash
source venv/Scripts/activate
```

### 3. Install Dependencies
```powershell
pip install -r requirements.txt
```

---

## 🏃 Running the Application

To start the Gradio app:
```powershell
python app.py
```

- The app will launch a local web server (usually at `http://127.0.0.1:7860`).
- It will also provide a public Gradio share link if enabled.
- The `get_roster_details` function is automatically exposed as an MCP tool.

## 🛠️ Project Structure
- `app.py`: Main Gradio application.
- `requirements.txt`: Python dependencies.
- `compdb.db`: SQLite database containing the roster data.
- `venv/`: Virtual environment directory.

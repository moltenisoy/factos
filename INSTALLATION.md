# Installation Guide

## Prerequisites

- Windows 10 or Windows 11
- Python 3.7 or higher
- Administrator privileges

## Step 1: Install Python

If you don't have Python installed:

1. Download Python from https://www.python.org/downloads/
2. Run the installer
3. **Important**: Check "Add Python to PATH" during installation
4. Complete the installation

## Step 2: Install Dependencies

Open Command Prompt as Administrator and run:

```bash
cd path\to\factos
pip install -r requirements.txt
```

## Step 3: Run the Application

### Method 1: Using the batch file
Double-click `run.bat`

### Method 2: Using Command Prompt
```bash
python main.py
```

The application will automatically request administrator privileges if needed.

## Troubleshooting

### "Python is not recognized"
- Make sure Python is added to PATH
- Restart Command Prompt after installing Python

### "No module named PyQt5"
- Run: `pip install PyQt5`

### Application doesn't start
- Make sure you're running as Administrator
- Check if Python 3.7+ is installed: `python --version`

### Switch doesn't change color
- The optimization may have failed
- Check if you have administrator privileges
- Some optimizations require a system restart to take effect

## First Time Use

1. Launch the application
2. Review each optimization category
3. Click the red switches to enable desired optimizations
4. Or click "Apply All Optimizations" to enable everything
5. The switches will turn green when optimizations are active

## Safety

- All changes are backed up automatically
- To revert: Simply toggle the green switch back to red
- Backups are stored in the `backups/` folder

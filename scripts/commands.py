import subprocess
from app.core.log_config import logger

def start_ngrok_in_background(command: str) -> None:
    result = subprocess.run(command, capture_output=True)
    stdout = result.stdout.decode("utf-8")
    stderr = result.stderr.decode("utf-8")
    
    if result.returncode != 0:
        logger.error(f"Command failed: {' '.join(command)}\n{stderr}")
        raise subprocess.CalledProcessError(result.returncode, command)
    
    if stdout:
        logger.info(stdout)
    if stderr:
        logger.warning(stderr)
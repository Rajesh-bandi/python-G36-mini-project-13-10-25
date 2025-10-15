from task_tracker.main import app

# Vercel's Python runtime expects an ASGI 'app' object at module-level.
# This file is the serverless entrypoint used by Vercel when deploying from the GUI.

__all__ = ("app",)

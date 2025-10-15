from task_tracker.main import app

# Vercel serverless entrypoint; exposes a module-level `app` ASGI application.
__all__ = ("app",)

from webhook_server import app

if __name__ == "__main__":
    import os
    port = int(os.environ.get('PORT', 4242))
    app.run(port=port)

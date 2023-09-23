import webview

# Create a GUI window to view the HTML content
webview.create_window(
    'quizzapp', 
    'https://google.com',
    x=100,  # Adjust the x-coordinate as needed
    y=100,  # Adjust the y-coordinate as needed
    width=700,  # Adjust the width as needed
    height=700,  # Adjust the height as needed
    resizable=True  # Allow resizing if desired
)

# Start the webview
webview.start()


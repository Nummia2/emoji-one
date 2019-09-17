import json
"""
  This function assumes that index.html will try to load main.js
  from /default/main.js. 
  You can modify your index.html script tag to be: 
  <script src="/default/main.js"></script>
"""
def lambda_handler(event, context):
        
    path = event.get('path', {})
    resultPage = None
    result = {
        "statusCode": 200,
        "headers": {
        'Content-Type': 'text/html',
        },
        "body": resultPage
    }
    if path == "/main.js":
        with open('main.js', 'r') as f:
            resultPage = f.read() 
        result["headers"]["Content-Type"] = "text/javascript;charset=UTF-8"
    elif path == "/package.json":
        with open('package.json', 'r') as f:
            resultPage = f.read()
        result["headers"]["Content-Type"] = "application/json"
    elif path == "/index.html":
        with open('index.html', 'r') as f:
            resultPage = f.read()
    else:
        with open('index.html', 'r') as f:
            resultPage = f.read()
    result["body"] = resultPage
    return result

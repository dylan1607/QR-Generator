<html>
    <body>
        <h1>QR Code Generator</h1>
        <img src='./application.png'>
        <h2>Intro</h2>
        <p>
        Web Application is created with HTML/CSS and JS with backend Python by using EEL, which a little Python library with full access to Python capabilities and library
        </p>
        <p>
            You can generate QR Code with this simple way. Add some text and after that you click the button the image will appear
        </p>
        <div><i>The directory structure of the project is simple:</i></div>
        <div>
            .<br>
            ├── main.py<br>
            ├── README.md<br>
            ├── requirements.txt<br>
            └── web<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── index.html<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── script.js<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── css<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── style.css <br>
        </div>
        <h2>Getting Started</h2>
        <ul>
            <li>Clone the repo and cd into the directory</li>
            <blockquote>
                $ git clone https://github.com/dylan1607/QR-Generator.git <br>
                $ cd QR-Generator
            </blockquote>
            <li>Require Python 3.x. Install eel, pyqrcode and pypng</li>
            <blockquote>
                $ pip install eel pyqrcode pypng<br>
                or<br>
                $ pip install -r requirements.txt
            </blockquote>
            <li>Run the application</li>
            <blockquote>$ python main.py</blockquote>
        </ul>
    <body>        
</html>

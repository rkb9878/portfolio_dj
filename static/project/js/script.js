let theamDots = document.getElementsByClassName('theam-dot');

let theme=localStorage.getItem('theme');
if (theme==null){
    setTheme('light');
}else{
    setTheme(theme);
}

for (var i = 0; theamDots.length > i; i++) {
    theamDots[i].addEventListener('click', function () {
        let mode = this.dataset.mode;
        console.log(mode);
        setTheme(mode);
    });
}

function setTheme(obj) {
    if (obj == 'light') {
        document.getElementById('theam-style').href = '' +
            'static/project/css/style.css';
    } else if (obj == 'green') {
        document.getElementById('theam-style').href = 'static/project/css/green.css ';
    } else if (obj == 'blue') {
        document.getElementById('theam-style').href = 'static/project/css/blue.css ';
    } else if (obj == 'purple') {
        document.getElementById('theam-style').href = 'static/project/css/pruple.css';
    }
    localStorage.setItem('theme',obj);
}

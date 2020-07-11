function user_choise(choise){
    const Http = new XMLHttpRequest();
    const url='https://localhost:5000/' + chise;
    Http.open("GET", url);
    Http.send();
}
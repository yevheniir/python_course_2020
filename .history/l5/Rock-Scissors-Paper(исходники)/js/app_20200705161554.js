function user_choise(choise){
    const Http = new XMLHttpRequest();
    const url='https://localhost:5000/' +;
    Http.open("GET", url);
    Http.send();
}
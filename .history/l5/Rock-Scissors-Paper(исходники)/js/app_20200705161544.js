function user_choise(choise){
    const Http = new XMLHttpRequest();
    const url='https://localhost:/posts';
    Http.open("GET", url);
    Http.send();
}
function user_choise(choise){
    const Http = new XMLHttpRequest();
    const url='https://localhos/posts';
    Http.open("GET", url);
    Http.send();
}